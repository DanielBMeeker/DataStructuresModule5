# 2 methods and a driver
# Noah Hobbs, Daniel Meeker, and Jacen LeCompte


class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.starting_node = None
        self.end_node = None

    def add_first(self, data):
        if not self.starting_node:
            new_node = Node(data)
            self.end_node = new_node
        else:
            new_node = Node(data)
            new_node.next_node = self.starting_node
            self.starting_node.prev_node = new_node
        self.starting_node = new_node
        return self.starting_node

    def search(self, value_to_find):
        current = self.starting_node
        found_flag = False
        search_complete = False
        if not self.starting_node:
            return "List is empty"
        while not search_complete:
            if current.data == value_to_find:
                found_flag = True
                search_complete = True
            else:
                current = current.next_node
                if current is None:
                    search_complete = True
        return f'is your value in the list? {found_flag}'


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.add_first(12)
    my_list.add_first(15)
    my_list.add_first(202)
    # This search should return true
    print(my_list.search(15))
    # this search should return false
    print(my_list.search(10))
