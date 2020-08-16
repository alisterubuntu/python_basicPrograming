'''
An array is also a data structure that stores a collection of items. Like lists, arrays are ordered, mutable, enclosed in square brackets, and able to store non-unique items.

But when it comes to the array’s ability to store different data types, the answer is not as straightforward. It depends on the kind of array used.

To use arrays in Python, you need to import either an array module or a NumPy
'''

import array as arr
array_1 = arr.array("i", [3, 6, 9, 12])
print(array_1)
print(type(array_1))


import numpy as np
array_2 = np.array(["numbers", 3, 6, 9, 12])
print (array_2)
print(type(array_2))
'''
So What’s the Difference?

Now that we know their definitions and features, we can talk about the differences between lists and arrays in Python:

    Arrays need to be declared. Lists don’t, since they are built into Python. In the examples above, you saw that lists are created by simply enclosing a sequence of elements into square brackets. Creating an array, on the other hand, requires a specific function from either the array module (i.e., array.array()) or NumPy package (i.e., numpy.array()). Because of this, lists are used more often than arrays.
    Arrays can store data very compactly and are more efficient for storing large amounts of data.
    Arrays are great for numerical operations; lists cannot directly handle math operations. For example, you can divide each element of an array by the same number with just one line of code. If you try the same with a list, you’ll get an error.

'''

array = np.array([3, 6, 9, 12])
division = array/3
print(division)
print (type(division))


'''
list = [3, 6, 9, 12]
division = list/3
TypeError                                 Traceback (most recent call last)
 in ()
      1 list = [3, 6, 9, 12]
----> 2 division = list/3

TypeError: unsupported operand type(s) for /: 'list' and 'int'
'''