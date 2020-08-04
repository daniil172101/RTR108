Python 3.6.9 (default, Jul 17 2020, 12:50:27) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> camels = 42
>>> '%d' % camels
'42'
>>> 'I have spotted %d camels.' % camels
'I have spotted 42 camels.'
>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
>>> '%d %d %d' % (1, 2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    '%d %d %d' % (1, 2)
TypeError: not enough arguments for format string
>>> '%d' % 'dollars'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    '%d' % 'dollars'
TypeError: %d format: a number is required, not str
>>> 
