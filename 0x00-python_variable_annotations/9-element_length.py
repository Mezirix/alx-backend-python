#! /usr/bin/env python3
'''Task 9's module.
'''
from typing import Iterable, List, sequence, Tuple


def element_length(Ist: Iterable [Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in Ist]
