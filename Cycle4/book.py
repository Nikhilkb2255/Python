class publisher:
   
    def __init__(self):
        self.publish = input("Enter the name of publisher : ")
   
    def display(self):
        print("\n Name of the publisher : ",self.publish)


class book(publisher):
   
    def __init__(self):
        self.title = input("Enter the title of book : ")
        self.author = input("Enter the name of author : ")
       
        super().__init__()
    
    def display(self):
        print("\n Title of the book : ", self.title)
        print("\n Name of author : ",self.author)
       
        super().display()

class python(book):
    
    def __init__(self):
      
        super().__init__()
        
        self.price = input("Enter the price of book : ") 
        self.page = input("Enter the no. of pages : ")

    def display(self):

        super().display()

        print("\n Price of book : ",self.price)
        print("\n Total pages of the book : ",self.page)

x = python()
x.display()
