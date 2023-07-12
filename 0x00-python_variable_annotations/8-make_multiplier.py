#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make multiplier (multiplier: float) -> Callable[[float], float]:
'''Creates a multiplier function.
'''
return lambda x: x * multiplier
