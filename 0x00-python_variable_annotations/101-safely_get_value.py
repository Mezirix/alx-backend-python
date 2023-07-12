#!/usr/bin/env python3
 '''Task 11's module.
 '''
from typing import Any, Mapping, Union, Typevar


T = TypeVar ('T')
Res = Union [Any, T]
Def = Union [T, None]


def safely_ get_value(dct: Mapping, key: Any, default: Def = None) -› Res:
'''Retrieves a value from a dict using a given key.
'''
if key in dct:
    return dct[key]
else:
    return default
