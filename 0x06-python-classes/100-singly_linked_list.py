#!/usr/bin/python3
"""Module of class Node and SinglyLinkedList"""


class Node:
    """Defines a node of a singly linked list

    Attributes:
        data (int): node's data
        next_node (`obj`: Node, optional): the next node
    """

    def __init__(self, data, next_node=None):
        """__init__ method doc"""
        self.__data = check_attr(data, int, "data must be an integer")
        self.__next_node = check_attr(next_node, Node,
        "next_node must be a Node object")

    @property
    def data(self):
        """Returns the data of the current node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the current node data to value"""
        self.__data = check_attr(value, int, "data must be an integer")

    @property
    def next_node(self):
        """Returns the node following the current node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the current node next_node to value"""
        self.__next_node = check_attr(value, Node,
        "next_node must be a Node object")


class SinglyLinkedList:
    """Class that defines a sinlgy linked list

    Attributes:
        head (Node): the linked list's head

    """
    def __init__(self):
        """__init__ method doc"""
        self.__head = None

    def __str__(self):
        """__str__ method doc"""
        s = ""
        tmp = self.__head
        while tmp is not None:
            if tmp != self.__head:
                s += "\n"
            s += str(tmp.data)
            tmp = tmp.next_node
        return s

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list
        (increasing order)"""
        value = check_attr(value, int, "data must be an integer")
        tmp = self.__head
        prev = None
        while tmp is not None:
            if value <= tmp.data:
                break
            prev = tmp
            tmp = tmp.next_node
        if prev is not None:
            prev.next_node = Node(value, tmp)
        else:
            self.__head = Node(value, tmp)


def check_attr(value, typ, msg):
    """Checks if the value has the required type.
        Return this value if it's the case or raise an error otherwise

        Args:
            value (any type): the value to be checked
    """
    if isinstance(value, typ) or value is None:
        return value
    else:
        raise TypeError(msg)
