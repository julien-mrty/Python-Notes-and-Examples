""""""
"""
A set is a collection of unique objects. A basic use case is removing duplication:
"""
l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
print(set(l))
print(list(set(l)))

"""
Set elements must be hashable. The set type is not hashable, so you can’t build a set with nested set instances. But
frozenset is hashable, so you can have frozenset elements inside a set.

In addition to enforcing uniqueness, the set types implement many set operations as infix operators, so, given two sets 
a and b, a | b returns their union, a & b computes the intersection, a - b the difference, and a ^ b the symmetric 
difference.

Literal set syntax like {1, 2, 3} is both faster and more readable than calling the constructor (set([1, 2, 3])). The 
latter form is slower because, to evaluate it, Python has to look up the set name to fetch the constructor, then build
a list, and finally pass it to the constructor. In contrast, to process a literal like {1, 2, 3}, Python runs a 
specialized BUILD_SET bytecode.
"""

"""
Frozen Set:
"""
print(frozenset(range(10)))

"""
Set Comprehensions
"""
from unicodedata import name
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')})

"""
Note that the return value of & is a set. Even better: the set operators in dictionary views are compatible with set 
instances. Check this out:
"""
d1 = dict(a=1, b=2, c=3, d=4)
s = {'a', 'e', 'i'}
print(d1.keys() & s)
print(d1.keys() | s)
"""
A dict_items view only works as a set if all values in the dict are hashable. Attempting set operations on a dict_items 
view with an unhashable value raises TypeError: unhashable type 'T', with T as the type of the offending value. On the 
other hand, a dict_keys view can always be used as a set, because every key is hashable—by definition.
"""
