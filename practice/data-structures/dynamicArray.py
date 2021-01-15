class DynamicArray:
    def __init__(self):
        self._size = 0          # actual number of elements in dynamic array
        self._capacity = 1      # maximum capacity of the dynamic array
        self.array = self._create_array(self._capacity)
    def _create_array(self, capacity) -> list :
        '''
        Private function
        Create a new array with capacity
        '''
        return [None]*capacity
    def _resize(self) -> None:
        '''
        Private function
        Resize the array to new capacity
        '''
        self._capacity *= 2
        new_array = self._create_array(self._capacity)
        for i in range(self._size):
            new_array[i] = self.array[i]
        self.array = new_array
    def get_size(self) -> int :
        '''
        Get the length of the array.

        Returns:
        -------
        Int
            The length of the array.
        '''
        return self._size
    def append(self, item) -> None :
        '''
        Add a item to the end of the array

        Parameters
        ----------
        Item: 
            The element will be added to the end of the array.
        '''
        if (self._size >= self._capacity):
            self._resize()
        self.array[self._size] = item
        self._size += 1
    def pop(self):
        '''
        Pop the last item from the end of the array.

        Returns
        -------
        Item:
            The element is from the end of the array.
        
        Raises
        ------
        IndexError
            If there is no element in the array.
        '''
        if self._size > 0:
            self._size -= 1
            item, self.array[self._size] = self.array[self._size], None
            return item
        raise IndexError("There is no element in the array")
    def get_item(self, index):
        '''
        Get element at given index.

        Parameters
        ----------
        index (int):
            The index you want to know the element.

        Returns
        -------
        Item:
            The element at the specific index.
        
        Raises
        ------
        IndexError
            If the index is invalid.
        '''
        if(index>= 0 and self._size > index):
            return self.array[index]
        raise IndexError("Invalid index")
    def insert(self, item, index) -> None:
        '''
        Put the item at the specific index of the array.

        Parameters
        ----------
        Item:
            The element wants to put into the array.
        Index (int):
            The index you want to put into the element.
        
        Raises
        ------
        IndexError
            If the index larger than the array size.
        '''
        if self._size >= index:
            if (self._size >= self._capacity):
                self._resize()
            old_array = self.array
            self.array[index] = item
            self._size += 1
            for i in range(index+1, self._size):
                self.array[i] = old_array[i-1]
        else:
            raise IndexError("Invalid index")
    def remove_at(self, index):
        '''
        Remove the element at specific index from the array.

        Parameters
        ----------
        Index (int):
            The index you want to remove the element.
        
        Returns
        -------
        item:
            The element is from the specific index of the array.
        
        Raises
        ------
        IndexError
            If the index is larger than the size of array.
        '''
        if self._size > index:
            item = self.array[index]
            self._size -= 1
            for i in range(index, self._size):
                self.array[i] = self.array[i+1]
            self.array[self._size] = None
            return item
        raise IndexError("Invalid index")
    def is_empty(self) -> bool :
        '''
        Check the array is empty or not.

        Returns
        -------
        bool:
            If the array is empty return true, else return false.
        '''
        return self._size == 0
    def prepend(self,  item):
        '''
        Insert the item into the index 0 of the array.

        Parameters
        ----------
        item:
            The element wants to insert at the index 0 of the array.
        '''
        if (self._size >= self._capacity):
            self._resize()
        self._size += 1
        for i in range(self._size, 0, -1):
            self.array[i] = self.array[i-1]
        self.array[0] = item
    def find(self, item):
        '''
        Find out the index of item if the item is in the array.

        Parameters
        ----------
        item:
            The element which wants to know the index of it.

        Returns
        -------
            If the item in the array, reutrn the element of the index, else return -1.
        '''
        for i in range(self._size):
            if self.array[i] == item:
                return i
        return -1
