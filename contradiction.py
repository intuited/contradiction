"""Routines to compare dictionaries."""
import collections

def contradiction(dfrom, dto):
    """Compute the change from dfrom to dto.

    If both `dfrom` and `dto` are dict-derived,
    returns (result, value) where
    `result` is '==' or '!=';
    `value` is a dictionary of dictionaries with the keys:

    -   '+': keys present in dto but not dfrom
    -   '-': keys present in dfrom but not dto
    -   '==': keys present in both with equivalent values.
    -   '!=': keys present in both with differing values
        -   The values of this dictionary will contain
            recursively similar structures.

    If either or both of `dfrom` and `dto` is a non-dictionary,
    returns ('!=', (dfrom, dto)).

    Examples::

        >>> from pprint import pprint
        >>> from functools import partial
        >>> pp = partial(pprint, width=40)
        >>> contradiction({1: 'one', 2: 'two'}, {1: 'one', 2: 'two'})
        ('==', {1: 'one', 2: 'two'})
        >>> pp(contradiction({1: {1: 'one', 2: 'two'}}, {1: {1: 'one'}}))
        ('!=',
         {'!=': {1: {'-': {2: 'two'},
                     '==': {1: 'one'}}}})
        >>> pp(contradiction({0: 0, 1: {1: 'uno', 2: 'two'}},
        ...                  {0: 0, 1: {1: 'one'}}))
        ('!=',
         {'!=': {1: {'!=': {1: ('uno',
                                'one')},
                     '-': {2: 'two'}}},
          '==': {0: 0}})
    """
    if isinstance(dfrom, dict) and isinstance(dto, dict):
        results = collections.defaultdict(dict)

        keys = sorted(frozenset(k for d in (dfrom, dto) for k in d))
        for key in keys:
            if key not in dfrom:
                results['+'][key] = dto[key]
            elif key not in dto:
                results['-'][key] = dfrom[key]
            else:
                result, value = contradiction(dfrom[key], dto[key])
                results[result][key] = value
        if results.keys() == ['==']:
            return '==', dict(results['=='])
        else:
            return '!=', dict(results)
    else:
        if dfrom == dto:
            return '==', dfrom
        else:
            return '!=', (dfrom, dto)
