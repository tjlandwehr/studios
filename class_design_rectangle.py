# RECTANGLE

# A rectangle has a length and a width. A rectangle should be able to provide its area and perimeter. A 
# rectangle can indicate whether it is smaller than another rectangle in terms of area. A rectangle can 
# indicate whether it is in fact a square.

# This first example is Reggie's code
# class Rectangle:

#     def __init__(self, length, width):

#         self.length = length
#         self.width = width
        
#     def get_area(self):
#         return self.length * self.width

#     def get_perimeter(self):
#         return self.length * 2 + self.width * 2
    
#     def is_smaller(self, rhs):
#         return self.get_area() < rhs.get_area()
    
#     def is_square(self):
#         return self.length == self.width

# def main():
#     myrectangle = Rectangle(3, 4)
#     other_rectangle = Rectangle(5, 5)

#     print('area',myrectangle.get_area())
#     print('per',myrectangle.get_perimeter())
    
#     print('my square',myrectangle.is_square())
#     print('other square', other_rectangle.is_square())
#     print(myrectangle.is_smaller(other_rectangle))
#     print(other_rectangle.is_smaller(myrectangle))

# if __name__ == "__main__":
#     main()

class Rectangle:
    
    def __init__(self, init_length, init_width):
        """Create a new rectangle with the given length and width"""
        self.length = init_length
        self.width = init_width
        
    def get_perimeter(self):
        return 2 * self.length + 2 * self.width

    def get_area(self):
        return self.length * self.width

    def is_smaller_area(self, target):
        return self.get_area() < target.get_area()

    def is_square(self):
        return self.length == self.width

def main():
    p = Rectangle(3, 3)
    q = Rectangle(5, 12)

    print(p)
    print(q)
    print(p.get_perimeter())
    print(p.get_area())
    print(q.get_perimeter())
    print(q.get_area())
    print(p.is_smaller_area(q))
    print(q.is_smaller_area(p))
    print(p.is_square())
    print(q.is_square())

if __name__ == "__main__":
    main()