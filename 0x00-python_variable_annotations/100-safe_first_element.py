#!/usr/bin/env python3
'''Task 10's module.
'''
from typing import Any, sequence, Union


def safe_first_element (Ist: sequence [Any]) -> Union[Any, None]:
'''Retrieves the first element of a sequence if it exists.
'''
if Ist:
    return lst[0]
else:
    return None
