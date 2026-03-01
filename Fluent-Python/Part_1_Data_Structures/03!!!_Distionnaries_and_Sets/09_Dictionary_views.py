""""""
"""
The dict instance methods .keys(), .values(), and .items() return instances of classes called dict_keys, dict_values,
and dict_items, respectively. These dictionary views are read-only projections of the internal data structures used in
the dict implementation. They avoid the memory overhead of the equivalent Python 2 methods that returned lists 
duplicating data already in the target dict, and they also replace the old methods that returned iterators.
"""
d = dict(a=10, b=20, c=30)
values = d.values()
print(values)
print(len(values))
print(list(values))
print(reversed(values))

d['z'] = 99
print(d)
print(values)