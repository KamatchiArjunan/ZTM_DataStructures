#Array implementation

class Array():
  def __init__(self):
    self.length = 0
    self.data = {}

  def __str__(self):
    return str(self.__dict__) #returns the class object as a dictionary

  def get(self,index):
    return self.data[index]

  def push(self, item):
    self.length += 1
    self.data[self.length - 1] = item
    return "Item pushed"

  def pop(self):
    last_item = self.data[self.length - 1]
    del self.data[self.length - 1]
    self.length -= 1
    return last_item

  def insert(self, index, item):
    self.length += 1
    for i in range(self.length-1, index, -1):
      self.data[i] = self.data[i-1]
    self.data[index] = item
    return "Item inserted"

  def delete(self, index):
    deleted_item = self.data[index]
    for i in range(index, self.length-1):
      self.data[i] = self.data[i+1]
    del self.data[self.length-1] #delete the last item which is present twice
    self.length = self.length - 1
    return deleted_item

array = Array()
print(array.push(1))
print(array.push(2))
print(array.push(3))
print(array.push(4))
print(array.get(0))
print(array.push(5))
print(array.pop())
print(array.insert(4,5))
print(array.delete(2))
print(array)
