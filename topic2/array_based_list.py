"""
Program: array_based_list.py
Author: Daniel Meeker
Date: 10/04/2020
OS: Windows 10
IDE: Pycharms

This program uses the basic python list to mimic a standard
float array like you might make in Java. Using this array-like
object it creates a linked list with all associated methods.

* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""
import random


class LinkedListEmptyException(Exception):
    pass


class LinkedListFullException(Exception):
    pass


class LinkedList:
    """
    LinkedList Class
    """
    def __init__(self, max_size=5):
        """
        LinkedList constructor
        :param max_size: optional - defaults to 5
        """
        self._current = 0
        self._head = 0
        self._next = 1
        self._max_size = max_size
        self._arr = [0 for j in range(self._max_size)]

    def insert(self, item):
        """
        Inserts an item to the end of the LinkedList. Raises
        an exception if the LinkedList is full.
        :param item: required
        :return: void
        """
        if not self.is_full():
            self._arr[self._head] = item
            self._head += 1
            self._next += 1
        else:
            raise LinkedListFullException("Linked List is Full")

    def remove(self):
        """
        Removes an item from the end of the LinkedList. Raises
        an exception if the LinkedList is empty.
        :return: float
        """
        if not self.is_empty():
            temp = self._arr[self._head - 1]
            self._arr[self._head - 1] = None
            self._head -= 1
            self._next -= 1
            return temp
        else:
            raise LinkedListEmptyException("Linked List is Empty")

    def replace(self, item, index):
        """
        Removes and replaces the element at 'index' with 'item
        :param item: required
        :param index: required
        :return: void
        """
        self._arr[index] = item

    def peek(self):
        """
        Returns the item at the end of the LinkedList without removing it
        :return: float
        """
        if not self.is_empty():
            return self._arr[self._head - 1]
        else:
            raise LinkedListEmptyException("Linked List is Empty")

    def is_full(self):
        """
        If full returns true, else returns false
        :return: boolean
        """
        return self._next > self._max_size

    def is_empty(self):
        """
        If empty returns true, else returns false
        :return: boolean
        """
        return self._head == 0

    def size(self):
        """
        Returns the Size of the LinkedList
        :return: int
        """
        return self._head - 1

    def print(self):
        """
        Returns all the contents of the LinkedList in order
        :return: string
        """
        if not self.is_empty():
            output = ""
            for i in range(self.size() + 1):
                output += str(self._arr[i]) + "\n"
        else:
            raise LinkedListEmptyException("Linked List is Empty")
        return output


if __name__ == '__main__':
    """
    I decided to use random numbers to decide the size of the LinkedList
    and the numbers to get added to the LinkedList
    """
    size = random.randint(5, 10)
    print(size)
    float_list = LinkedList(size)
    for x in range(size):
        number_to_add = round(random.uniform(1, 100), 2)
        float_list.insert(number_to_add)
    # test the print function
    print("----------")
    print(float_list.print())
    # test the is_full exception
    print("----------")
    print(float_list.is_full())
    # test adding to full list
    print("----------")
    try:
        float_list.insert(3.14)
    except LinkedListFullException as e:
        print(e)
    # test the peek function
    print("----------")
    print(float_list.peek())
    print("----------")
    # test the replace function
    float_list.replace(5, 2)
    print(float_list.print())
    print("----------")
    # test the remove function
    print(float_list.remove())
    print(float_list.print())
    # re-test the is_full exception
    print("----------")
    print(float_list.is_full())
    # empty this list
    print("----------")
    for x in range(size):
        try:
            print(str(float_list.remove()) + " removed")
        except LinkedListEmptyException as e:
            print(e)
    # try to peek on empty list
    print("----------")
    try:
        print(float_list.peek())
    except LinkedListEmptyException as e:
        print(e)
    # try to print empty list
    print("----------")
    try:
        print(float_list.print())
    except LinkedListEmptyException as e:
        print(e)
    # add another item to now empty list
    float_list.insert(1)
    print(float_list.print())
