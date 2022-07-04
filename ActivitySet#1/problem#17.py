x~/python101-Thanushree293-7$ ipython
bash: ipython: command not found
~/python101-Thanushree293-7$ python
Python 3.8.12 (default, Sep 10 2021, 00:16:05) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> re.match(r"[aeiou]","a")
<re.Match object; span=(0, 1), match='a'>
>>> re.match(r"[aeiou]","b")
>>> re.match(r"[aeiou]","a")
<re.Match object; span=(0, 1), match='a'>
>>> re.match(r"[aeiou]","b")
>>> re.match(r"[abeiou]","b")
<re.Match object; span=(0, 1), match='b'>
>>> x=re.match(r"[abeiou]","b")
>>> x=re.match(r"[donkey]","d)
  File "<stdin>", line 1
    x=re.match(r"[donkey]","d)
                             ^
SyntaxError: EOL while scanning string literal
>>> x=re.match(r"[donkey]","d")
>>> x
<re.Match object; span=(0, 1), match='d'>
>>> x=re.match(r"[donkey]","s")
>>> x
>>> re.match(r"[donkey]","s")
>>> x=re.match(r"[donkey]","s")
>>> x
>>> x=re.match(r"[donkey]","d")
>>> x
<re.Match object; span=(0, 1), match='d'>
>>> re.match(r"[aeiou]","s")
>>> re.match(r"[aeiou]","e")
<re.Match object; span=(0, 1), match='e'>
>>> re.match(r"[^xyz]","e")
<re.Match object; span=(0, 1), match='e'>
>>> re.match(r"[^xyz]","x")
>>> re.match(r"[^xyz]","r")
<re.Match object; span=(0, 1), match='r'>
>>> re.match(r"[a-z0-9]","a")
<re.Match object; span=(0, 1), match='a'>
>>> re.match(r"[a-z0-9]","b")
<re.Match object; span=(0, 1), match='b'>
>>> re.match(r"[a-z0-9]","aa")
<re.Match object; span=(0, 1), match='a'>
>>> re.match(r"[a-z0-9]","3")
<re.Match object; span=(0, 1), match='3'>
>>> re.match(r"[a-z0-9]","a3")
<re.Match object; span=(0, 1), match='a'>
>>> re.match(r"[a-z0-9]","3n")
<re.Match object; span=(0, 1), match='3'>
>>> x=re.match(r"[a-z0-9]","3n")
>>> x
<re.Match object; span=(0, 1), match='3'>
>>> dir(x)
['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']
>>> x.groups()
()
>>> x.pos
0
>>> x=re.search(r"[a-z0-9]","3n")
>>> x
<re.Match object; span=(0, 1), match='3'>
>>> x=re.search(r"[a-z0-9]","3n","e")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.8/re.py", line 201, in search
    return _compile(pattern, flags).search(string)
  File "/usr/lib/python3.8/re.py", line 304, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.8/sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.8/sre_parse.py", line 948, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
TypeError: unsupported operand type(s) for &: 'str' and 'int'
>>> x=re.search(r"[a-z0-9]","3n")
>>> x
<re.Match object; span=(0, 1), match='3'>
>>> x=re.search(r"[a-z0-9]","abc")
>>> x
<re.Match object; span=(0, 1), match='a'>
~/python101-Thanushree293-7$ python
Python 3.8.12 (default, Sep 10 2021, 00:16:05) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> re.match(r"[^X.*:]","s")
<re.Match object; span=(0, 1), match='s'>
>>> re.match(r"[^X.*:]","z")
<re.Match object; span=(0, 1), match='z'>
>>> re.match(r"[^X.*:]","3")
<re.Match object; span=(0, 1), match='3'>
>>> X-sir: sff.44 innocent
  File "<stdin>", line 1
    X-sir: sff.44 innocent
              ^
SyntaxError: invalid syntax
>>> X-sir: sff.44 innocent
  File "<stdin>", line 1
    X-sir: sff.44 innocent
              ^
SyntaxError: invalid syntax
>>> X-sir: sff 44 innocent
  File "<stdin>", line 1
    X-sir: sff 44 innocent
               ^
SyntaxError: invalid syntax
>>> X-sir: sff innocent
  File "<stdin>", line 1
    X-sir: sff innocent
               ^
SyntaxError: invalid syntax
>>> X-sir: sff
  File "<stdin>", line 1
SyntaxError: illegal target for annotation
>>> z=X-sir: sff44 innocent
  File "<stdin>", line 1
    z=X-sir: sff44 innocent
           ^
SyntaxError: invalid syntax
>>> 