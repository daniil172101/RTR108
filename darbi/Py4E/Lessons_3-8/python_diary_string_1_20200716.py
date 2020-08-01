Python 3.6.9 (default, Jul 17 2020, 12:50:27) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter =fruit[1]
>>> print(letter)
a
>>> letter =fruit[0]
>>> print(letter)
b
>>> letter =fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    letter =fruit[1.5]
TypeError: string indices must be integers
>>> len(fruit)
6
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    last = fruit[length]
NameError: name 'length' is not defined
>>> length = len(fruit)
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> last = fruit[length-1]
>>> print(last)
a
>>> 
