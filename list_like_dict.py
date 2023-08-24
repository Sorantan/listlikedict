from collections import UserDict
from typing import Any

class ListLikeDict(UserDict):
    def __init__(self, dict_=None, /, **kwarg):
        if dict_ is not None:
            for k in dict_.keys():
                if isinstance(k, int):
                    raise KeyError("cannot use integer in keys")
        super().__init__(dict_, **kwarg)

    def __getitem__(self, key: Any) -> Any:
        if isinstance(key, slice):
            return self[tuple(self.keys())[key]]
        elif isinstance(key, tuple):
            return [self[k] for k in key]
        elif key in self.data:
            return self.data[key]
        elif isinstance(key, int):
            return self[tuple(self.keys())[key]]
        else:
            return super().__getitem__(key)
        
    def __setitem__(self, key: Any, item: Any) -> None:
        if isinstance(key, slice):
            self[tuple(self.keys())[key]] = item
        elif isinstance(key, tuple):
            try:
                len(item)
            except TypeError:
                raise ValueError(f"could not set '{type(item).__name__}' into list")
            if not len(key) == len(item):
                raise ValueError(f"could not set from length {len(item)} item into length {len(key)} item")
            for k, v in zip(key, item):
                self[k] = v
        elif key in self.data:
            self.data[key] = item
        elif isinstance(key, int):
            self[tuple(self.keys())[key]] = item
        else:
            super().__setitem__(key, item)

