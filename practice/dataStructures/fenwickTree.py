class FewnickTree:
    def __init__(self, array: [int]):
        self.data = array
        self.size = len(array)
        self.tree = self.construction()
    def construction(self) -> [int]:      
        array = [0]
        array = array + self.data.copy()
        for i in range(1, self.size+1):
            parent = i + self.lsb(i)
            if (parent < self.size+1):
                array[parent] = array[parent] + array[i]
        return array
    def prefix_sum(self, index: int) -> int:
        '''
        the index starts with 1 not 0
        '''
        result = 0
        while index != 0:
            result = result + self.tree[index]
            index = index - self.lsb(index)
        return result
    def range_sum_query(self, start: int, end: int) -> int:
        return self.prefix_sum(end) - self.prefix_sum(start)
    def lsb(self, index: int) -> int:
        '''
        return the value that how many numbers this index is responsible for include itself.
        '''
        return index & -index