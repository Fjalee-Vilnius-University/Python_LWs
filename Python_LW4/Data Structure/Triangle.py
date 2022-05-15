class Vector(object):
    '''
    Data type for triangle. has functions to find area and perimeter
    To create triangle the constructor takes 3 float numbers (length of sides).
    '''
    def __init__(self,l1,l2,l3):
        if isinstance(l1,float) and isinstance(l2,float) and isinstance(l3,float):
            self.l1 = l1
            self.l2 = l2
            self.l3 = l3
            if (not (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1)):
                raise TypeError("Error, triangle can't be made out of lengths " + str(l1) + " " + str(l2) + " " + str(l3))
        else: raise TypeError("Error, triangle expects float sides lengths.")
    def __str__(self):
        return "triangle with sides " + str(self.l1) + " " + str(self.l2) + " " + str(self.l3)
        
    

a = Vector(2.0, 3.0, 4.0)
