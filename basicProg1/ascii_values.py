c = "h"
print("the ascii values is {}".format(ord(c)))

longstring = "hello this is " \
             "common india"

print(ord(longstring))

'''
Traceback (most recent call last):
  File "/home/alister/Documents/pycharm_projects/python_basicPrograming/basicProg1/ascii_values.py", line 7, in <module>
    print(ord(longstring))
TypeError: ord() expected a character, but string of length 26 found
'''