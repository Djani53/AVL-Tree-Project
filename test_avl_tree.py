import pytest
from avl_tree import AVLTree


# ── Z: Zero ──────────────────────────────────────────────
class TestZero:
    def test_empty_tree_size(self):
        tree = AVLTree()
        assert tree.size() == 0

    def test_empty_tree_contains(self):
        tree = AVLTree()
        assert tree.contains(5) is False

    def test_empty_tree_to_list(self):
        tree = AVLTree()
        assert tree.to_list() == []


# ── O: One ───────────────────────────────────────────────
class TestOne:
    def test_insert_one_element(self):
        tree = AVLTree()
        tree.insert(10)
        assert tree.size() == 1

    def test_contains_inserted_element(self):
        tree = AVLTree()
        tree.insert(10)
        assert tree.contains(10) is True

    def test_to_list_one_element(self):
        tree = AVLTree()
        tree.insert(10)
        assert tree.to_list() == [10]

    def test_delete_only_element(self):
        tree = AVLTree()
        tree.insert(10)
        tree.delete(10)
        assert tree.size() == 0
        assert tree.contains(10) is False


# ── M: Many ──────────────────────────────────────────────
class TestMany:
    def test_insert_multiple_elements(self):
        tree = AVLTree()
        for val in [5, 3, 7, 1, 4]:
            tree.insert(val)
        assert tree.size() == 5

    def test_to_list_sorted(self):
        tree = AVLTree()
        for val in [5, 3, 7, 1, 4]:
            tree.insert(val)
        assert tree.to_list() == [1, 3, 4, 5, 7]

    def test_contains_multiple(self):
        tree = AVLTree()
        for val in [5, 3, 7]:
            tree.insert(val)
        assert tree.contains(3) is True
        assert tree.contains(9) is False


# ── B: Boundary ──────────────────────────────────────────
class TestBoundary:
    def test_no_duplicates(self):
        tree = AVLTree()
        tree.insert(5)
        tree.insert(5)
        assert tree.size() == 1

    def test_delete_nonexistent(self):
        tree = AVLTree()
        tree.insert(5)
        tree.delete(99)  # Darf keinen Fehler werfen
        assert tree.size() == 1

    def test_avl_balance_after_inserts(self):
        """Rechtslastiger Insert soll trotzdem sortierte Liste ergeben."""
        tree = AVLTree()
        for val in [1, 2, 3, 4, 5]:  # Würde ohne AVL entarten
            tree.insert(val)
        assert tree.to_list() == [1, 2, 3, 4, 5]

    def test_delete_with_two_children(self):
        tree = AVLTree()
        for val in [5, 3, 7, 1, 4, 6, 8]:
            tree.insert(val)
        tree.delete(5)
        assert tree.contains(5) is False
        assert tree.size() == 6


# ── I: Interface ─────────────────────────────────────────
class TestInterface:
    def test_all_methods_exist(self):
        tree = AVLTree()
        assert hasattr(tree, "insert")
        assert hasattr(tree, "delete")
        assert hasattr(tree, "contains")
        assert hasattr(tree, "size")
        assert hasattr(tree, "to_list")


# ── E: Exceptions ────────────────────────────────────────
class TestExceptions:
    def test_insert_returns_none(self):
        tree = AVLTree()
        result = tree.insert(5)
        assert result is None

    def test_delete_empty_tree(self):
        tree = AVLTree()
        tree.delete(5)  # Darf keinen Fehler werfen
        assert tree.size() == 0


# ── S: Simplest ──────────────────────────────────────────
class TestSimplest:
    def test_single_rotation_right(self):
        """Links-Links-Fall: Rechtsrotation nötig."""
        tree = AVLTree()
        for val in [3, 2, 1]:
            tree.insert(val)
        assert tree.to_list() == [1, 2, 3]

    def test_single_rotation_left(self):
        """Rechts-Rechts-Fall: Linksrotation nötig."""
        tree = AVLTree()
        for val in [1, 2, 3]:
            tree.insert(val)
        assert tree.to_list() == [1, 2, 3]