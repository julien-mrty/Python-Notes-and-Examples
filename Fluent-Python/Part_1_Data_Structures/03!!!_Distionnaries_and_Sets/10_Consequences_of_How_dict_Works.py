""""""
"""
The hash table implementation of Python’s dict is very efficient, but it’s important to understand the practical effects 
of this design:
• Keys must be hashable objects. They must implement proper __hash__ and __eq__ methods.
• Item access by key is very fast. A dict may have millions of keys, but Python can locate a key directly by computing 
  the hash code of the key and deriving an index offset into the hash table, with the possible overhead of a small number 
  of tries to find a matching entry.
• Key ordering is preserved as a side effect of a more compact memory layout for dict in CPython 3.6, which became an 
  official language feature in 3.7.
• Despite its new compact layout, dicts inevitably have a significant memory overhead. The most compact internal data
  structure for a container would be an array of pointers to the items (tuple). Compared to that, a hash table needs to
  store more data per entry, and Python needs to keep at least one-third of the hash table rows empty to remain 
  efficient.
• To save memory, avoid creating instance attributes outside of the __init__ method.
"""