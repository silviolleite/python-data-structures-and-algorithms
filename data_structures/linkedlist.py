"""
Linked List

This module demonstrates how to create a linked list class.

Linked lists are an ordered collection of objects. So what makes them different from normal lists? Linked lists
differ from lists in the way that they store elements in memory. While lists use a contiguous memory block to store
references to their data, linked lists store references as part of their own elements.

Linked lists serve a variety of purposes in the real world. They can be used to implement queues or
stacks as well as graphs. They’re also useful for much more complex tasks, such as lifecycle management for an
operating system application.

"""

from data_structures.node import Node
from typing import List, Optional, Iterator, Any


class LinkedList:

    def __init__(self, nodes: Optional[List] = None) -> None:
        """
        This is called when a new LinkedList object is instantiated

        :param nodes: (list) The start list (default None)
        """
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self) -> str:
        """
        Representation of the LinkedList object instances

        :return: (str) official string representation
        """
        current = self.head
        items = []
        while current:
            items.append(current.data)
            current = current.next
        items.append(None)
        return "".join(str(items))

    def __iter__(self) -> Iterator:
        """
        The method through the list and yields every single node.
        The most important thing to remember about this is that you need to always validate that
        the current node is not None.
        When that condition is True, it means you’ve reached the end of your linked list.

        :return: void
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node: Node) -> None:
        """
        Add a new node as the first position in the linked list

        :param node: (Node) The new node instance to add the linked list
        :return: void
        """
        node.next = self.head
        self.head = node

    def add_last(self, node: Node) -> None:
        """
        Add a new node at the last position in the linked list

        :param node: (Node) The new node instance to add the linked list
        :return: void
        """
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data: Any, new_node: Node) -> None:
        """
        Add a new node after the given target value from the linked list

        :param target_node_data: The target data value
        :param new_node: (Node) The new node instance to add after the given target value from the linked list
        :return: void
        :raises:
            Exception: List is empty
            Exception: Node with data '%s' not found
        """
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data: Any) -> None:
        """
        Remove the node by value

        :param target_node_data: value to remove from linked list
        :return: void
        :raises:
            Exception: List is empty
            Exception: Node with data '%s' not found
        """

        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return

            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


def main():
    """
    >>> llist = LinkedList([23, 35, 10, 50])
    >>> llist
    [23, 35, 10, 50, None]
    >>> llist.add_last(Node(5))
    >>> llist
    [23, 35, 10, 50, 5, None]
    >>> llist.remove_node(35)
    >>> llist
    [23, 10, 50, 5, None]
    >>> llist.add_after(50, Node(15))
    >>> llist
    [23, 10, 50, 15, 5, None]
    >>> llist.add_first(Node(1))
    >>> llist
    [1, 23, 10, 50, 15, 5, None]
    >>> for node in llist:
    ...     node.data
    1
    23
    10
    50
    15
    5
    >>> new_llist = LinkedList()
    >>> new_llist.add_after(0, Node(1))
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/doctest.py", line 1328, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.main[12]>", line 1, in <module>
        new_llist.add_after(0, Node(1))
      File "/Users/silvioleite/Projects/python-list/data_structures/linkedlist.py", line 44, in add_after
        raise Exception("List is empty")
    Exception: List is empty
    >>> llist.remove_node(100)
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/doctest.py", line 1328, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.main[13]>", line 1, in <module>
        llist.remove_node(100)
      File "/Users/silvioleite/Projects/python-list/data_structures/linkedlist.py", line 72, in remove_node
        raise Exception("Node with data '%s' not found" % target_node_data)
    Exception: Node with data '100' not found
    >>> llist.add_after(200, Node(15))
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/doctest.py", line 1328, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.main[14]>", line 1, in <module>
        llist.add_after(200, Node(15))
      File "/Users/silvioleite/Projects/python-list/data_structures/linkedlist.py", line 52, in add_after
        raise Exception("Node with data '%s' not found" % target_node_data)
    Exception: Node with data '200' not found
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

