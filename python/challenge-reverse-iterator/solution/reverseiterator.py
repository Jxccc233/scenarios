class ReverseIterator:
    """A class that implements an iterator that iterates over the elements of data in reverse order"""

    def __init__(self, data: list):
        """Initialize the iterator with a list of integers data.
        
        Args:
            data(list):A list of integers data, e.g. [1,2,3,4,5]    
        """
        self.data = data
        self.index = len(data) - 1

    def __next__(self) -> int:
        """Return the next value from the iteration. Return None when the iteration has ended.
        
        Args:
            self: the iterator object
        
        Returns:
            value(int): the next value from the iteration, or None when the iteration has ended
        """
        if self.index >= 0:
            value = self.data[self.index]
            self.index -= 1
            return value
        else:
            return None

    def __iter__(self) -> 'ReverseIterator':
        """Return the iterator object itself.
        
        Args:
            self: the iterator object

        Returns:
            the iterator object itself
        """
        return self