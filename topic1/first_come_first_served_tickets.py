"""
Program: first_come_first_served_tickets.py
Author: Daniel Meeker
Date: 10/03/2020
OS: Windows 10
IDE: Pycharms

This program uses a queue to sell tickets to a line of customers
in order until the tickets are gone or the line is emtpy. I copied
and pasted my own Queue class into this file for ease of uploading.

* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""
import random


class QueueEmptyException(Exception):
    pass


class QueueFullException(Exception):
    pass


class Queue:
    """
    Queue Class
    """
    def __init__(self, max_size=5):
        self.head = 0
        # self.tail = 0 not used because of my use of the built-in remove function for
        # Python lists which adjusts the indexes of the queue automatically.
        self.queue_size = 0  # changed the name to self.queue_size because it was causing
        # errors with the size() function. I first tried changing the size function to a
        # property setter but ran into some maximum recursion errors.
        self.max_size = max_size  # used to limit size of Queue. Defaults to 5.
        self.items = []  # adjusted this so that instead a list of blank spaces it is just
        # an empty list so that I could more easily track the size of the queue

    def is_empty(self):
        """
        If there are no elements in the queue this will return true,
        otherwise it will return false
        :return: boolean
        """
        if self.size() == 0:
            return True
        else:
            return False

    def is_full(self):
        """
        If the number of elements in the queue are equal to its self.max_size
        this will return true, otherwise it will return false.
        :return:
        """
        if self.size() == self.max_size:
            return True
        else:
            return False

    def enqueue(self, item):
        """
        This function will take an item and add it to the end of the queue
        I handled wrap around by using the Python list built in remove function
        in the dequeue function which automatically adjusts the indexes of each
        item in the queue so that this implementation doesn't have to worry
        about wrap around.
        :param item: required
        :return: void
        """
        if not self.is_full():
            self.items.append(item)
        else:
            raise QueueFullException("Queue is Full")

    def dequeue(self):
        """
        I was having issues with wrap around so I decided to
        use the Python list function list.remove(item) where item
        is equal to self.peek() so that it grabs the first element.
        I did it that way instead of using the pop() function so that
        when 'item = self.peek()' runs it will throw the QueueEmptyException.
        I thought it was an elegant solution and made my brain hurt less than
        trying to make wrap around work.

        :return: first item of whatever data type is in the list
        """
        try:
            item = self.peek()
            self.items.remove(item)
            return item
        except QueueEmptyException:
            raise QueueEmptyException("Queue is Empty")

    def peek(self):
        if not self.is_empty():
            item_str = self.items[self.head]
            return item_str
        else:
            raise QueueEmptyException("Queue is Empty")

    def size(self):
        self.queue_size = len(self.items)
        return self.queue_size

    def print_queue(self):
        if not self.is_empty():
            stack_str = ""
            for x in range(self.size()):
                stack_str += str(self.items[x]) + "\n"
            return stack_str
        else:
            raise QueueEmptyException("Queue is Empty")


"""
Ticket Selling program:
"""


def sell_tickets(number_of_tickets):
    """
    This function will take in the number of available
    tickets and sell tickets to a queue of customers
    until the tickets are sold out or the line is empty.
    The number of customers varies with each run between
    1 and 1000. The number of tickets sold to each customer
    varies between 1-4 for each customer.
    :param number_of_tickets: required
    :return: a string
    """
    size_of_line = random.randint(1, 1000)
    total_tickets = number_of_tickets
    running_total = 0
    customer_line = Queue(size_of_line)
    for i in range(size_of_line):
        customer_line.enqueue("Customer " + str(i + 1))
    while number_of_tickets > 0:
        ticket_sale = random.randint(1, 4)
        if (running_total + ticket_sale) > total_tickets:
            return "Sold Out! " + str(running_total) + " tickets sold. " + str(customer_line.size()) + " customers still in line"
        running_total += ticket_sale
        number_of_tickets -= ticket_sale
        try:
            customer_line.dequeue()
        except QueueEmptyException:
            return "All Customers Helped! " + str(number_of_tickets) + " tickets remain."
    if running_total == total_tickets:
        return "Sold Out! " + str(running_total) + " tickets sold. " + str(customer_line.size()) + " customers still in line"


if __name__ == '__main__':
    print("Simulation with 10 tickets: " + sell_tickets(10))
    print("Simulation with 100 tickets: " + sell_tickets(100))
    print("Simulation with 1000 tickets: " + sell_tickets(1000))
