import random

import numpy as np
from nose import with_setup

from pyspf.formula import TermEnum


def setup():
    """
    Setup.
    :return: None.
    """
    np.random.seed(37)
    random.seed(37)


def teardown():
    """
    Teardown.
    :return: None.
    """
    pass


@with_setup(setup, teardown)
def test_get_extractor():
    """
    Tests get extractor.

    :return: None.
    """
    record = {
        'x1': 20,
        'x2': 5,
        'a': 'left',
        'b': 'mid'
    }
    terms = [
        'Intercept',
        "C(a, levels=profile['a'])[T.right]",
        "C(b, levels=profile['b'])[T.mid]",
        "C(b, levels=profile['b'])[T.high]",
        'x1',
        'x2']
    expected = [
        TermEnum.INT,
        TermEnum.LVL,
        TermEnum.LVL,
        TermEnum.LVL,
        TermEnum.CON,
        TermEnum.CON
    ]

    for i, term in enumerate(terms):
        extractor = TermEnum.get_extractor(record, term)
        lhs = expected[i]
        rhs = extractor._type
        # print(extractor)
        assert lhs == rhs
