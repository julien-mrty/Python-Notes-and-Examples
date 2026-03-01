"""""""""
OrderedDict, ChainMap, Counter, and Shelf are ready to use but can also be customized by subclassing. In contrast, 
UserDict is intended only as a base class to be extended.

It’s better to create a new mapping type by extending collections.UserDict rather than dict. We realize that when we try 
to extend our StrKeyDict0 from 05_Automatic_handling_of_missing_keys to make sure that any keys added to the mapping are
stored as str.

The main reason why it’s better to subclass UserDict rather than dict is that the built-in has some implementation 
shortcuts that end up forcing us to override methods that we can just inherit from UserDict with no problems.

Note that UserDict does not inherit from dict, but uses composition: it has an internal dict instance, called data, 
which holds the actual items. This avoids undesired recursion when coding special methods like __setitem__, and
simplifies the coding of __contains__, compared to 05_Automatic_handling_of_missing_keys.

Thanks to UserDict, StrKeyDict is more concise than StrKeyDict0 05_Automatic_handling_of_missing_keys., but it does 
more: it stores all keys as str, avoiding unpleasant surprises if the instance is built or updated with data containing 
nonstring keys.
"""
import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item