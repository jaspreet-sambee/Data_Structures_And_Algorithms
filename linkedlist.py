from node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        temp_node = self.get_head_node()
        string_list = ""
        while(temp_node):
            string_list += str(temp_node.get_value()) + "\n"
            temp_node = temp_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.value == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while(current_node):
                if current_node.get_next_node().get_value() == value_to_remove:
                    current_node.set_next_node(current_node.get_next_node().get_next_node())
                    current_node = None
                else:
                    current_node = current_node.get_next_node()




ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

