class LinkedListEmptyException(Exception):
    pass


class LinkedListFullException(Exception):
    pass


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, can):
        new_node = Node(can)
        new_node.next_node = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next_node is not None:
            n = n.next_node
        n.next_node = new_node

    def delete_first(self):
        if self.head is None:
            raise LinkedListEmptyException("Linked List is Empty")
        self.head = self.head.next_node

    def delete_last(self):
        if self.head is None:
            raise LinkedListEmptyException("Linked List is Empty")
        n = self.head
        while n.next_node is not None:
            n = n.next_node
        n.next_node = None

    def replace(self, old, new):
        if self.head is None:
            raise LinkedListEmptyException("Linked List is Empty")

        n = self.head
        while n.next_node is not None:
            if n.next_node.data == old:
                n.next_node.data = new
                n = n.next_node

        if n.next_node is None:
            print("item not found in the list")
        else:
            n.next_node = n.next_node.next_node

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next_node


class CanMeeker:
    """
    Can Class
    """

    def __init__(self, company=None, content=None, size=None, price=None):
        """
        * Constructor for the Can class *
        Python does not allow for multiple constructors
        so to get around that I made all the parameters
        optional
        :param company: - optional
        :param content: - optional
        :param size: - optional
        :param price: optional
        """
        self._company = company  # underscores to indicate private variables
        self._content = content
        self._size = size
        self._price = price

    """
    Getters and Setters
    """

    def get_company(self):
        """
        company getter
        :return: string
        """
        return self._company

    def set_company(self, company_name):
        """
        company setter
        :param company_name: required
        :return: none
        """
        self._company = company_name

    def get_content(self):
        """
        content getter
        :return: string
        """
        return self._company

    def set_content(self, contents):
        """
        content setter
        :param contents: required
        :return: none
        """
        self._content = contents

    def get_size(self):
        """
        size getter
        :return: double
        """
        return self._size

    def set_size(self, size_of_can):
        """
        size setter
        :param size_of_can: required
        :return: none
        """
        self._size = size_of_can

    def get_price(self):
        """
        price getter
        :return: double
        """
        return self._price

    def set_price(self, price_of_can):
        """
        price setter
        :param price_of_can: required
        :return: none
        """
        self._price = price_of_can

    """
    Class Methods
    """

    def __str__(self):
        """
        overrides built-in function
        :return: a string
        """
        return ("{self._size} oz can of {self._company} {self._content} "
                "for ${self._price}").format(self=self)

    def __repr__(self):
        """
        overrides built_in function
        :return: a string that mimics the constructor
        """
        return ("{self.__class__.__name__}(company='{self._company}', "
                "contents='{self._content}', size={self._size}, price={self._price})").format(self=self)

    def display(self):
        return ("{self._size} oz can of {self._company} {self._content} "
                "for ${self._price}").format(self=self)


if __name__ == '__main__':
    new_linked_list = LinkedList()
    new_linked_list.insert_first(10)
    new_linked_list.insert_first(20)
    new_linked_list.insert_first(30)
    new_linked_list.insert_first(40)
    new_linked_list.insert_first(50)
    print(new_linked_list.print_list())
    new_linked_list.delete_first()
    print(new_linked_list.print_list())
    new_linked_list.delete_last()
    print(new_linked_list.print_list())
