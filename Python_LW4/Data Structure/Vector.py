class Vector(object):
    '''
    Data type for recreating 2D vectors. You can multiply two vectors using method "multiply"
    '''
    def __init__(self,x,y):
        if isinstance(x,int) and isinstance(y,int):
            self.x = x
            self.y = y
        else: raise TypeError("Wrong type! Vector expects integer coordinates!")
    def __str__(self):
        return "{%s,%s}" %(self.x, self.y)
    def multiply(self,another_vector):
      if isinstance(another_vector,Vector):
        return self.x * another_vector.x + self.y * another_vector.y
      else: raise TypeError("Wrong type! Vector can be multiplied only by vector!") 