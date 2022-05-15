class Vector(object):
    '''
    Data type for triangle. has functions to find area and perimeter. Has function to change lengths
    To create triangle the constructor takes 3 float numbers (length of sides).
    '''
    def __init__(self,l1,l2,l3):
        self.change_sides(l1,l2,l3)

    def __str__(self):
        return "triangle with sides " + str(self.l1) + " " + str(self.l2) + " " + str(self.l3)

    def change_sides(self,l1,l2,l3):
        if isinstance(l1,float) and isinstance(l2,float) and isinstance(l3,float):
            if (not (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1)):
                raise TypeError("Error, triangle can't be made out of lengths " + str(l1) + " " + str(l2) + " " + str(l3))
            else:
                self.l1 = l1
                self.l2 = l2
                self.l3 = l3
        else: raise TypeError("Error, triangle expects float sides lengths.")

    def perimeter(self):
        return self.l1 + self.l2 + self.l3 

    def area(self):
        s = self.perimeter()/2
        a = self.l1
        b = self.l2
        c = self.l3
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
        
a = Vector(2.0, 3.0, 4.0)
print(a.perimeter())
print(a.area())

a.change_sides(5.0,6.0,7.0)
print(a.perimeter())
print(a.area())
