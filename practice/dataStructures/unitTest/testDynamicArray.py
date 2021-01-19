import unittest
from practice.dataStructures.dynamicArray import DynamicArray

class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.DArray = DynamicArray()
    def test_append(self):
        self.DArray.append(3)
        self.assertEqual(self.DArray._size, 1)
        self.assertEqual(self.DArray.array[0], 3)
    def test_pop(self):
        self.DArray.append(3)
        self.DArray.append(4)
        item = self.DArray.pop()
        self.assertEqual(item, 4)
        self.assertEqual(self.DArray._size, 1)
    def test_get_size(self):
        self.assertEqual(self.DArray.get_size(), 0)
        self.DArray.append(3)
        self.assertEqual(self.DArray.get_size(), 1)
        self.DArray.append(4)
        self.DArray.append(5)
        self.DArray.pop()
        self.assertEqual(self.DArray.get_size(), 2)
    def test_get_item(self):
        self.DArray.append(3)
        self.DArray.append(4)
        self.DArray.append(5)
        self.assertEqual(self.DArray.get_item(1), 4)
    def test_insert(self):
        self.DArray.append(3)
        self.DArray.append(4)
        self.DArray.append(5)
        self.DArray.insert(6,1)
        self.assertEqual(self.DArray.get_item(1), 6)
        self.assertEqual(self.DArray.get_size(), 4)
    def test_remove_at(self):
        self.DArray.append(3)
        self.DArray.append(4)
        self.DArray.append(5)
        self.assertEqual(self.DArray.remove_at(1), 4)
        self.assertEqual(self.DArray.get_size(),2)
    def test_is_empty(self):
        self.assertEqual(self.DArray.is_empty(),True)
        self.DArray.append(3)
        self.DArray.append(4)
        self.DArray.append(5)
        self.assertEqual(self.DArray.is_empty(),False)
    def test_prepend(self):
        self.DArray.append(3)
        self.DArray.append(4)
        self.DArray.append(5)
        self.DArray.append(7)
        self.DArray.prepend(6)
        self.assertEqual(self.DArray.array[0], 6)
        self.assertEqual(self.DArray.array[1], 3)
        self.assertEqual(self.DArray.array[2], 4)
        self.assertEqual(self.DArray.array[3], 5)
        self.assertEqual(self.DArray.array[4], 7)
    def test_find(self):
        self.DArray.append(3)
        self.DArray.append(4)
        self.DArray.append(5)
        self.assertEqual(self.DArray.find(4), 1)
