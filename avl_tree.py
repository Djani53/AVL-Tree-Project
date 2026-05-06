class AVLNode:
    """Repräsentiert einen einzelnen Knoten im AVL-Baum."""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: "AVLNode | None" = None
        self.right: "AVLNode | None" = None
        self.height: int = 1


class AVLTree:
    """
    Implementiert eine geordnete Menge als AVL-Baum.
    Garantiert O(log n) für Einfügen, Suchen und Löschen.
    """

    def __init__(self) -> None:
        self.root: AVLNode | None = None
        self._size: int = 0

    # ── Öffentliche API ───────────────────────────────────────

    def insert(self, value: int) -> None:
        """Fügt einen Wert in den Baum ein. Duplikate werden ignoriert."""
        new_root, inserted = self._insert_recursive(self.root, value)
        self.root = new_root
        if inserted:
            self._size += 1

    def delete(self, value: int) -> None:
        """Entfernt einen Wert aus dem Baum, falls vorhanden."""
        self.root, deleted = self._delete_recursive(self.root, value)
        if deleted:
            self._size -= 1

    def contains(self, value: int) -> bool:
        """Gibt True zurück, wenn der Wert im Baum enthalten ist."""
        node = self.root
        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def size(self) -> int:
        """Gibt die Anzahl der Elemente im Baum zurück."""
        return self._size

    def to_list(self) -> list[int]:
        """Gibt alle Elemente sortiert als Liste zurück (In-Order-Traversal)."""
        result: list[int] = []
        self._inorder(self.root, result)
        return result

    # ── Private Hilfsmethoden ────────────────────────────────

    def _get_height(self, node: AVLNode | None) -> int:
        """Gibt die Höhe eines Knotens zurück (0 für None)."""
        return node.height if node else 0

    def _get_balance(self, node: AVLNode | None) -> int:
        """Balancefaktor = Höhe(links) - Höhe(rechts)."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _update_height(self, node: AVLNode) -> None:
        """Aktualisiert die gespeicherte Höhe eines Knotens."""
        node.height = 1 + max(
            self._get_height(node.left),
            self._get_height(node.right)
        )

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """
        Rechtsrotation um Knoten y.
            y              x
           / \            / \
          x   T3   →    T1   y
         / \                / \
        T1  T2            T2  T3
        """
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """
        Linksrotation um Knoten x.
          x                y
         / \              / \
        T1   y    →      x   T3
            / \         / \
           T2  T3      T1  T2
        """
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)
        return y

    def _balance(self, node: AVLNode) -> AVLNode:
        """Balanciert den Knoten falls nötig (alle 4 Rotationsfälle)."""
        self._update_height(node)
        balance = self._get_balance(node)

        # Links-Links-Fall → Rechtsrotation
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        # Links-Rechts-Fall → Erst Links-, dann Rechtsrotation
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Rechts-Rechts-Fall → Linksrotation
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        # Rechts-Links-Fall → Erst Rechts-, dann Linksrotation
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node  # Bereits balanciert

    def _insert_recursive(
        self, node: AVLNode | None, value: int
    ) -> tuple[AVLNode, bool]:
        """Rekursives Einfügen. Gibt (neuer_knoten, wurde_eingefügt) zurück."""
        if node is None:
            return AVLNode(value), True

        if value < node.value:
            node.left, inserted = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right, inserted = self._insert_recursive(node.right, value)
        else:
            return node, False  # Duplikat – nichts tun

        return self._balance(node), inserted

    def _get_min_node(self, node: AVLNode) -> AVLNode:
        """Gibt den Knoten mit dem kleinsten Wert im Teilbaum zurück."""
        current = node
        while current.left:
            current = current.left
        return current

    def _delete_recursive(
        self, node: AVLNode | None, value: int
    ) -> tuple[AVLNode | None, bool]:
        """Rekursives Löschen. Gibt (neuer_knoten, wurde_gelöscht) zurück."""
        if node is None:
            return None, False

        deleted = False
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
        else:
            deleted = True
            # Fall 1: Kein oder ein Kind
            if node.left is None:
                return node.right, deleted
            elif node.right is None:
                return node.left, deleted
            # Fall 2: Zwei Kinder → Inorder-Nachfolger (kleinster Wert rechts)
            successor = self._get_min_node(node.right)
            node.value = successor.value
            node.right, _ = self._delete_recursive(node.right, successor.value)

        return self._balance(node), deleted

    def _inorder(self, node: AVLNode | None, result: list[int]) -> None:
        """In-Order-Traversal: Links → Wurzel → Rechts (ergibt sortierte Folge)."""
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)