class rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def area(self):
        return self.length * self.width
    def peri(self):
        return 2*(self.length + self.width)

l1 = int(input("Enter length of rectangle 1 :"))
w1 = int(input("Enter width of rectangle 1 :"))
l2 = int(input("Enter length of rectangle 2 :"))
w2 = int(input("Enter width of rectangle 2 :"))
rect1 = rectangle(l1,w1)
rect2 = rectangle(l2,w2)

print("Area of 1st rectangle is ",rect1.area(),"Area of 2nd rectanlge is ",rect2.area())
print("Perimeter of 1st rectangle is ",rect1.peri(),"Area of 2nd rectanlge is ",rect2.peri())
