#!/usr/bin/python3
"""The Modules defines the SinglyLinkedList class
"""


class Node:
    """A Node in the list
    """

    def __init__(self, data: int, next_node=None) -> None:
        """The Node initializer

        Args:
            data (int): Data held by the node
            next_node (Node, optional): The next node in the list.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self) -> int:
        """The `data` getter

        Returns:
            int: The `data`
        """
        return self.__data

    @data.setter
    def data(self, data: int) -> None:
        """The `data` setter

        Args:
            data (int): The `data` of this node

        Raises:
            TypeError: if data is not an integer
        """
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self):
        """The `next_node` getter

        Returns:
            Node: The next node or None
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        """The `next_node` setter

        Args:
            node (Node): The next node

        Raises:
            TypeError: If `node` is not of type `Node`
        """
        if not (node is None or isinstance(node, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = node


class SinglyLinkedList:
    """A singly linked list
    """

    def __init__(self) -> None:
        """The instance initializer
        """
        self.__head = None

    def __str__(self) -> str:
        """The string rep of the class instance

        Returns:
            str: The items in the list arranged in a line
        """
        head = self.__head
        values = []

        while head:
            values.append(str(head.data))
            head = head.next_node
        return '\n'.join(values)

    def sorted_insert(self, value):
        """Insert a new node in a sorted other to the list

        Args:
            value (int): The value of the new node
        """
        head = self.__head
        prev = None
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
            return

        while head:
            if head.data >= value:
                if prev:
                    prev.next_node = new_node
                else:
                    self.__head = new_node
                new_node.next_node = head
                return
            prev = head
            head = head.next_node
        prev.next_node = new_node


if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(34)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    print(sll)
