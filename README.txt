``contradiction``
=================

Routines to compare dictionaries.

For now at least, this library consists of just the function `contradiction`.

Help on function contradiction in contradiction:

contradiction.contradiction = contradiction(dfrom, dto)
    Compute the change from dfrom to dto.
    
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



License
-------

`contradiction` is licensed under the FreeBSD license.
See the file COPYING for details.
