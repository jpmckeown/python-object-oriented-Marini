# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
    self.__hidden = "secret attribute"

  def getpages(self):
    return self.pages
  
class Magazine:
  def __init__(self, title):
    self.title = title

# TODO: create instances of the class
b1 = Book("War and Peace","Leo Tolstoy",1225)
m1 = Magazine("Military Modelling")

# TODO: print the class and property
print(type(m1))
print(isinstance(b1,Book))
# print(book1.getpages())
# print(book1._Book__hidden)