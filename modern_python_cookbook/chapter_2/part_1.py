import re
import os
import difflib
import fnmatch

# fnmatch can be used to match paterns inside strings

# the * wildcard
print(fnmatch.fnmatch('hello.txt', '*.txt'))

# using for patterns

a = 'a:b:c'
b = 'name:date:age'
c = 'veronica:vianey'

print(fnmatch.fnmatch(a ,'*:*:*'))

print(fnmatch.fnmatch(b ,'*:*:*'))

print(fnmatch.fnmatch(c ,'*:*:*'))

# use for filename enumeration feed a list and get lst that matches query
# find all text files

print(fnmatch.filter(os.listdir() ,'*.txt'))

# fnmatch.translate bridges betwwen fnmatch patterns and regular expressions
# eg findall png and jpg files
# import re


feg = '({})|({})'.format(fnmatch.translate('*.png'), fnmatch.translate('*.jpg'))

print(feg)

d = [s for s in os.listdir() if re.match(feg, s)]
print(d)

# finding text that is similar but not equal
# find diferences between sequences with difflib
# import difflib

# compute similarities and rate them from 0 and 1
s = 'today the weather is nice'

s1 = 'today the weather was nice'

s2 = 'today the waether is nice'

s3 = 'today my dog ate steak'
print(difflib.SequenceMatcher(None, s, s1, False).ratio())

print(difflib.SequenceMatcher(None, s, s2, False).ratio())

print(difflib.SequenceMatcher(None, s, s3,
False).ratio())
  
