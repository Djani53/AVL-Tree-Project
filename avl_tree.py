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

    def insert(self, value: int) -> None:
        """Fügt einen Wert in den Baum ein. Duplikate werden ignoriert."""
        pass

    def delete(self, value: int) -> None:
        """Entfernt einen Wert aus dem Baum, falls vorhanden."""
        pass

    def contains(self, value: int) -> bool:
        """Gibt True zurück, wenn der Wert im Baum enthalten ist."""
        pass

    def size(self) -> int:
        """Gibt die Anzahl der Elemente im Baum zurück."""
        pass

    def to_list(self) -> list[int]:
        """Gibt alle Elemente sortiert als Liste zurück (In-Order-Traversal)."""
        pass

    def _get_height(self, node: "AVLNode | None") -> int:
        """Hilfsmethode: Gibt die Höhe eines Knotens zurück."""
        pass

    def _get_balance(self, node: "AVLNode | None") -> int:
        """Hilfsmethode: Gibt den Balancefaktor eines Knotens zurück."""
        pass

    def _rotate_left(self, node: "AVLNode") -> "AVLNode":
        """Hilfsmethode: Führt eine Linksrotation durch."""
        pass

    def _rotate_right(self, node: "AVLNode") -> "AVLNode":
        """Hilfsmethode: Führt eine Rechtsrotation durch."""
        pass

    def _balance(self, node: "AVLNode") -> "AVLNode":
        """Hilfsmethode: Balanciert den Teilbaum ab dem gegebenen Knoten."""
        pass

    def _insert_recursive(self, node: "AVLNode | None", value: int) -> "AVLNode":
        """Hilfsmethode: Rekursives Einfügen."""
        pass

    def _delete_recursive(self, node: "AVLNode | None", value: int) -> "AVLNode | None":
        """Hilfsmethode: Rekursives Löschen."""
        pass

    def _inorder(self, node: "AVLNode | None", result: list[int]) -> None:
        """Hilfsmethode: In-Order-Traversal."""
        pass