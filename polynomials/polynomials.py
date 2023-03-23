from numbers import Number, Integral
import numpy as np


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):

        if isinstance(other, Number):
            coefs = tuple(element*other for element in self.coefficients)
            return Polynomial(coefs)
        
        elif isinstance(other,Polynomial):

            def unitmult(n):
            
                coeffs=tuple(np.zeros(n)) + self.coefficients
                return Polynomial(coeffs)
            newpol=Polynomial((0,))
            for c, d in enumerate(other.coefficients):
               newpol += d*unitmult(c)
            return newpol
        
        else:
            return NotImplemented 
    
    def __rmul__(self, other):

        return self * other

    def __sub__(self, other):

        return self + other * -1

    def __rsub__(self, other):

        return (self-other) * -1

    def __pow__(self, other):

        if isinstance(other, Integral) and other : 
            newpol=Polynomial((1,))
            n=1
            while n <= other : 
                newpol=self*newpol
                n+=1
            return newpol
        else:
            return NotImplemented

    def __call__(self, other):
        if isinstance(other,Number) :
            return sum(d*(other**c) for c, d in enumerate(self.coefficients))

        else :
            return NotImplemented

    def dx(self):
        if len(self.coefficients) == 1 :
            return Polynomial((0,))
        else:
            return Polynomial(tuple(c*d for c, d in
            enumerate(self.coefficients[1:], start=1)))

def derivative(obj):

    if isinstance(obj, Polynomial):
        return obj.dx()

    else:
        return NotImplemented