"""
Project 8 - Heaps - Solution Code
CSE 331 Fall2022
Onsay
"""

from typing import TypeVar, List

T = TypeVar('T')


class MinHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
        Gets the length of the array representing the min-heap
        :return: number of nodes in the min-heap
        """
        return len(self.data)
        pass

    def empty(self) -> bool:
        """
        Determines if the min-heap is empty
        :return: True if the min-heap has no nodes and False otherwise
        """
        if len(self.data) == 0:
            return True
        return False
        pass

    def top(self) -> T:
        """
        Returns the root of the min-heap
        :return: The root of the min-heap
        """
        if self.empty():
            return None
        return self.data[0]
        pass

    def get_left_child_index(self, index: int) -> int:
        """
        Gets the index of the left child of the node with the given index
        :param index: Parent of the left child's index being returned
        :return: index of the left child of the node at index "index"
        """
        if index*2+1 >= len(self.data):
            return None
        return index*2+1
        pass

    def get_right_child_index(self, index: int) -> int:
        """
        Gets the index of the right child of the node with the given index
        :param index: Parent of the right child's index being returned
        :return: index of the right child of the node at index "index"
        """
        if index*2+2 >= len(self.data):
            return None
        return index*2+2
        pass

    def get_parent_index(self, index: int) -> int:
        """
        Gets the index of the parent of the node with the given index
        :param index: Child of the node's index being returned
        :return: index of the parent of the node at index "index"
        """
        if index > 0:
            return (index-1)//2
        return None
        pass

    def get_min_child_index(self, index: int) -> int:
        """
        Gets the index of the minimum child of node at index "index"
        :param index: Index of the node whose children are being evaluated
        :return: the index of the minimum child of node at index "index"
        """
        if self.get_right_child_index(index) is None:
            if self.get_left_child_index(index) is None:
                return None
            return self.get_left_child_index(index)
        left_i = self.get_left_child_index(index)
        right_i = self.get_right_child_index(index)
        if self.data[self.get_left_child_index(index)] < self.data[self.get_right_child_index(index)]:
            return self.get_left_child_index(index)
        return self.get_right_child_index(index)
        pass

    def percolate_up(self, index: int) -> None:
        """
        Swaps node at index "index" with its parent until its parent is less that it
        :param index: Index pf the node to percolate up
        """
        parent = self.get_parent_index(index)
        if index > 0 and self.data[index] < self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self.percolate_up(parent)
        pass

    def percolate_down(self, index: int) -> None:
        """
        Swaps node at index "index" with its minimum child until its children are both greater that it
        :param index: Index pf the node to percolate down
        """
        if self.get_left_child_index(index):
            left = self.get_left_child_index(index)
            small_child = left  # although right may be smaller
            if self.get_right_child_index(index):
                right = self.get_right_child_index(index)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[index]:
                self.data[index], self.data[small_child] = self.data[small_child], self.data[index]
                self.percolate_down(small_child)
        pass

    def push(self, val: T) -> None:
        """
        Inserts node with value "val" onto end of the min-heap and percolates it up into place
        :param val: Value of node to push
        """
        self.data.append(val)
        self.percolate_up(len(self.data) - 1)
        pass

    def pop(self) -> T:
        """
        Removes the minimum node (root) and reassembles the min-heap to keep it valid
        :return: Node that was popped
        """
        if not self.empty():
            self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
            removed = self.data.pop()
            self.percolate_down(0)
            return removed
        return None
        pass


class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = MinHeap()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    __repr__ = __str__

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.to_tree_format_string()
    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
        Determines if the max-heap is empty
        :return: True if the max-heap is empty and False otherwise
        """
        return self.data.empty()
        pass

    def top(self) -> int:
        """
        Returns root of the max-heap
        :return: The value of the root of the max-heap
        """
        if self.data.top() is None:
            return None
        return -self.data.top()
        pass

    def push(self, key: int) -> None:
        """
        Inserts the negative of value "key" into the end of the max-heap, then percolates up to
        fit min-heap properties
        :param key: The value to push onto the max-heap
        """
        self.data.push(-key)
        pass

    def pop(self) -> int:
        """
        Removes the smallest value from the max heap (largest when not negative) which is the root
        :return: the negative of the value that was popped
        """
        if self.empty():
            return None
        return -self.data.pop()
        pass


def get_eating_times(values: List[List[List[int]]]) -> List[List[int]]:
    """
    Determines the gaps in the inteervals in the given list
    :param values: A list of interval lists (each interval list corresponds to one family member)
    :return: A list of intervals that are not overlapped by the given list "values"
    """
    val_heap = MinHeap()
    open_intervals = []
    if len(values) == 0:
        return open_intervals

    for person in range(len(values)):
        for interval in values[person]:
            val_heap.push(interval)

    merged = [val_heap.data[0]]
    while len(val_heap.data) > 0:
        interval = val_heap.data[0]
        current = merged[len(merged) - 1]
        if (interval[0] <= current[0] <= interval[1]) or (current[0] <= interval[0] <= current[1]):
            current[0] = min(interval[0], current[0])
            current[1] = max(interval[1], current[1])
        else:
            merged.append(interval)
        val_heap.pop()

    if len(merged) < 1:
        return open_intervals

    for interval in range(len(merged) - 1):
        open_intervals.append([merged[interval][1], merged[interval + 1][0]])
    return open_intervals
    pass
