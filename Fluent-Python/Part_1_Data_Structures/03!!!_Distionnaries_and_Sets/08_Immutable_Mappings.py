""""""
"""
MappingProxyType
"""
from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
d[2] = 'B'
print(d_proxy)
print(d_proxy[2])

"""
Here is how this could be used in practice in the hardware programming scenario: the constructor in a concrete Board 
subclass would fill a private mapping with the pin objects, and expose it to clients of the API via a public .pins 
attribute implemented as a mappingproxy. That way the clients would not be able to add, remove, or change pins by 
accident.
"""