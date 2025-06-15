"""
That function takes a sequence of numbers and returns the sum of those numbers. So if you were to invoke sum([1,2,3]), the result would be 6. The challenge here is to write a mysum function that does the same thing as the built-in sum function. However, instead of taking a single sequence as a parameter, it should take a variable number of arguments. Thus, although you might invoke sum([1,2,3]), you’d instead invoke mysum(1,2,3) or mysum(10,20,30,40,50). 

NOTE: The built-in sum function takes an optional second argument, which we’re ignoring here. 

And no, you shouldn’t use the built-in sum function to accomplish this! (You’d be amazed just how often someone asks me this question when I’m teaching courses.)
"""
from numbers import Number,Complex

NumberType = (Number, Complex)

def mysum(*args):
    total = 0

    for el in args:
        if isinstance(el, NumberType):
            total += el
    
    return total

if __name__ == '__main__':
    print(mysum(5, 10, 'anwifhjwq'))