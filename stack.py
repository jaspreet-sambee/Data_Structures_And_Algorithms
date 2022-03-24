from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.size < self.limit:
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
    # Increment stack size by 1 here:
      self.size += 1
    else:
      print("All out of space!")
    

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  def peek(self):
    if self.size > 0:
	    return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  # Define has_space() and is_empty() below:
  def has_space(self):
    return self.size < self.limit

  def is_empty(self):
    return self.size == 0
  