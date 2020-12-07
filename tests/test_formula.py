import random

import numpy as np
from nose import with_setup

from pyspf.formula import TermEnum, InteractionExtractor


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


@with_setup(setup, teardown)
def test_basic_extractions():
    """
    Tests basic extractions.

    :return: None.
    """
    record = {
        'x1': 20.0,
        'x2': 5.0,
        'a': 'left',
        'b': 'mid'
    }
    terms = [
        'Intercept',
        "C(a, levels=profile['a'])[T.left]",
        "C(a, levels=profile['a'])[T.right]",
        "C(b, levels=profile['b'])[T.low]",
        "C(b, levels=profile['b'])[T.mid]",
        "C(b, levels=profile['b'])[T.high]",
        'x1',
        'x2',
        'a[left]', 'a[right]',
        'a[T.left]', 'a[T.right]',
        'b[low]', 'b[mid]', 'b[high]',
        'b[T.low]', 'b[T.mid]', 'b[T.high]'
    ]
    expected = [
        1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 20.0, 5.0,
        1.0, 0.0,
        1.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 1.0, 0.0
    ]

    for i, term in enumerate(terms):
        extractor = TermEnum.get_extractor(record, term)
        lhs = extractor.value
        rhs = expected[i]
        # print(f'{extractor._term}: {lhs}')
        assert lhs == rhs


@with_setup(setup, teardown)
def test_function_extractions():
    """
    Tests extractions of functions on continuous variables.

    :return: None.
    """
    record = {
        'x1': 20.0,
        'x2': 5.0
    }
    terms = [
        'x1',
        'x2',
        'np.abs(x1)',
        'np.log(x1)',
        'np.sin(x1)',
        'np.log(np.sin(x1))'
    ]
    expected = [
        20.0, 5.0, 20.0,
        2.995732273553991,
        0.9129452507276277,
        -0.09107936652955065
    ]

    for i, term in enumerate(terms):
        extractor = TermEnum.get_extractor(record, term)
        lhs = extractor.value
        rhs = expected[i]
        # print(f'{extractor._term}: {lhs}')
        assert lhs == rhs


@with_setup(setup, teardown)
def test_interaction_extractions():
    """
    Tests extractions of functions on continuous variables.

    :return: None.
    """
    record = {
        'x1': 20.0,
        'x2': 5.0,
        'a': 'left',
        'b': 'mid'
    }
    terms = [
        'Intercept',
        'x1',
        'x2',
        'x1:x2:a[left]',
        'x1:x2:a[right]',
        'x1:x2:b[T.low]',
        'x1:x2:b[T.mid]',
        'a[T.right]:b[T.low]', 'a[T.right]:b[T.mid]',
        'a[T.left]:b[T.mid]', 'a[T.left]:b[T.high]',
        "x1:x2:C(a, levels=profile['a'])[left]", "x1:x2:C(a, levels=profile['a'])[right]",
        "x1:x2:C(b, levels=profile['b'])[T.mid]", "x1:x2:C(b, levels=profile['b'])[T.high]",
        "np.abs(x1):a[T.left]"
    ]
    expected = [
        1.0,
        20.0,
        5.0,
        100.0,
        0.0,
        0.0,
        100.0,
        0.0, 0.0,
        1.0, 0.0,
        100.0,
        0.0,
        100.0,
        0.0,
        20.0
    ]

    for i, term in enumerate(terms):
        extractor = InteractionExtractor(record, term)
        lhs = extractor.value
        rhs = expected[i]
        # print(f'{extractor._terms}: {lhs}')
        assert lhs == rhs
