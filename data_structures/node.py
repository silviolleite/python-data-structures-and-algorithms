"""
Node

This module demonstrates how to create a simple Node class.
How you can see it has the two elements of every single node: 'data' and 'next'.

Data: contains the value to be stored in the node.
Next: contains a reference to the next node on the list.

"""
from typing import Any


class Node:
    """
    It represents each node of the list
    """

    def __init__(self, data: Any) -> None:
        """
        This is called when a new Node object is instantiated

        :param data: The node data value
        """
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        """
        Representation of the Node object instances

        :return: (str) official string representation
        """
        return self.data


def main():
    """
    >>> node = Node([1, 2])
    >>> type(node)
    <class '__main__.Node'>
    >>> node.data
    [1, 2]
    >>> node.next
    >>> node2 = Node(data=["a", "b"])
    >>> node2.data
    ['a', 'b']
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
