
class Circle: 

    def __init__(self, centr, rad):
        
        self.centre = centr
        self.radius = rad

    def __contains__(self, other):

        if len(other) == 2 :

            return sum((a-b)*(a-b) for a,b in zip(self.centre,other))<= self.radius*self.radius

        else:
            return NotImplemented
