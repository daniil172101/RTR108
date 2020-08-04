Python 3.6.9 (default, Jul 17 2020, 12:50:27) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: /home/danik/RTR108/darbi/Py4E/Lessons_3-8/python_files_1_20200717.py 
Line Count: 1909
>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
94625
>>> print(inp[:20])
From stephen.marquar
>>> fhand = open('mbox-short.txt')
>>> 
>>> print(len(fhand.read()))
94625
>>> print(len(fhand.read()))
0
>>> 
