"""Demonstrationsprogramm für den AVL-Baum als geordnete Menge."""
from avl_tree import AVLTree


def main() -> None:
    print("=== AVL-Baum Demonstration ===\n")

    tree = AVLTree()

    # Einfügen mehrerer Werte in zufälliger Reihenfolge
    values = [10, 5, 15, 3, 7, 12, 20, 1, 4]
    print(f"Einfügen: {values}")
    for v in values:
        tree.insert(v)

    print(f"Größe:         {tree.size()}")
    print(f"Sortiert:      {tree.to_list()}")
    print(f"Enthält 7:     {tree.contains(7)}")
    print(f"Enthält 99:    {tree.contains(99)}")

    # Löschen von Elementen
    print("\nLösche 5 und 15...")
    tree.delete(5)
    tree.delete(15)
    print(f"Sortiert:      {tree.to_list()}")
    print(f"Größe:         {tree.size()}")

    # Duplikate werden ignoriert
    print("\nFüge 10 nochmal ein (Duplikat)...")
    tree.insert(10)
    print(f"Größe (unverändert): {tree.size()}")

    # AVL-Balancierung bei aufsteigendem Einfügen
    print("\n=== Balancierungstest ===")
    balanced_tree = AVLTree()
    print("Einfügen aufsteigend: 1, 2, 3, 4, 5, 6, 7")
    for i in range(1, 8):
        balanced_tree.insert(i)
    print(f"Sortiert (AVL balanciert): {balanced_tree.to_list()}")
    print("Ohne AVL wäre das ein entarteter Baum mit O(n) Laufzeit!")


if __name__ == "__main__":
    main()