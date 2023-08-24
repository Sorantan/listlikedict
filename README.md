# List Like Dict

Python dict like list

# Get value
You can get values from dict like list

```Python
from list_like_dict impoer ListLikeDict

lld = ListLikeDict({"a" : 1, "b": 2, "c": 2, "d": 4, "e": 6, "f": 10})
print(lld)
# {'a': 1, 'b': 2, 'c': 2, 'd': 4, 'e': 6, 'f': 10}

print(lld[0])
# 1

print(lld[1,3,5])
# [2, 4, 10]

print(lld[0:5:2])
# [1, 2, 6]
```

# Set value
You can set values to dict like list

```Python
lld[2] = 'new'
print(lld)
# {'a': 1, 'b': 2, 'c': 'new', 'd': 4, 'e': 6, 'f': 10}

lld[-1,-2,-3] = ['negative one', 'negative two', 'negative three']
print(lld)
# {'a': 1, 'b': 2, 'c': 'new', 'd': 'negative three', 'e': 'negative two', 'f': 'negative one'}
```

# Exception
You can't use integer key
```Python
ListLikeDict({0: 'zero', 1: 'one'})
# KeyError: 'cannot use integer in keys'
```

Other exception
```Python
lld[20]
# IndexError: tuple index out of range

lld[0, 2] = 3
# ValueError: could not set 'int' into list

lld[0, 2] = [3, 5, 6, 6]
# ValueError: could not set from length 4 item into length 2 item
```

