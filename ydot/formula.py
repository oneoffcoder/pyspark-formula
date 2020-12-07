import importlib
from abc import ABC, abstractmethod
from enum import IntEnum
from functools import reduce

import pandas as pd


class TermEnum(IntEnum):
    """
    Term types.

    - CAT: categorical without levels specified
    - LVL: categorical with levels specified
    - CON: continuous
    - FUN: continuous with function transformations
    - INT: intercept
    """
    CAT = 1
    LVL = 2
    CON = 3
    FUN = 4
    INT = 5

    @staticmethod
    def get_extractor(record, term):
        """
        Gets the associated extractor based on the specified term.

        :param record: Dictionary.
        :param term: Model term.
        :return: Extractor.
        """

        if term.startswith('C'):
            return LvlExtractor(record, term)
        elif '[' in term and ']' in term:
            return CatExtractor(record, term)
        elif 'Intercept' == term:
            return IntExtractor(record, term)
        elif '(' in term and ')' in term:
            return FunExtractor(record, term)
        else:
            return ConExtractor(record, term)


class Extractor(ABC):
    """
    Extractor to get value based on model term.
    """

    def __init__(self, record, term, term_type):
        """
        ctor.

        :param: Dictionary.
        :term: Model term.
        :term_type: Type of term.
        :return: None
        """
        self._record = record
        self._term = term
        self._type = term_type

    def __repr__(self):
        return f'{self.__class__.__name__}[term={self._term}, type={self._type.name}]'

    @property
    @abstractmethod
    def value(self):
        """
        Gets the extracted value.
        """
        pass


class CatExtractor(Extractor):
    """
    Categorical extractor (no levels).
    """

    def __init__(self, record, term):
        """
        ctor.

        :param record: Dictionary.
        :param term: Model term.
        :return: None.
        """
        super().__init__(record, term, TermEnum.CAT)

    @property
    def value(self):
        idx = self._term.index('[')
        x_name = self._term[0:idx]

        if x_name not in self._record or self._record[x_name] is None:
            return None

        lhs = self._term.rindex('[') + 1
        rhs = self._term.rindex(']')
        x_val = self._term[lhs:rhs]
        x_val = x_val.replace('T.', '')

        if self._record[x_name] == x_val:
            return 1.0
        return 0.0


class LvlExtractor(Extractor):
    """
    Categorical extractor (with levels).
    """

    def __init__(self, record, term):
        """
        ctor.

        :param record: Dictionary.
        :param term: Model term.
        :return: None.
        """
        super().__init__(record, term, TermEnum.LVL)

    @property
    def value(self):
        lhs = self._term.index('(') + 1
        rhs = self._term.index(',')
        x_name = self._term[lhs:rhs]

        if x_name not in self._record or self._record[x_name] is None:
            return None

        lhs = self._term.rindex('[') + 1
        rhs = self._term.rindex(']')
        x_val = self._term[lhs:rhs]
        x_val = x_val.replace('T.', '')

        if self._record[x_name] == x_val:
            return 1.0
        return 0.0


class ConExtractor(Extractor):
    """
    Continuous extractor (no functions).
    """

    def __init__(self, record, term):
        """
        ctor.

        :param record: Dictionary.
        :param term: Model term.
        :return: None.
        """
        super().__init__(record, term, TermEnum.CON)

    @property
    def value(self):
        return self._record[self._term] if self._term in self._record else None


class IntExtractor(Extractor):
    """
    Intercept extractor. Always returns 1.0.
    """

    def __init__(self, record, term):
        """
        ctor.

        :param record: Dictionary.
        :param term: Model term.
        :return: None.
        """
        super().__init__(record, term, TermEnum.INT)

    @property
    def value(self):
        return 1.0


class FunExtractor(Extractor):
    """
    Continuous extractor (with functions defined).
    """

    def __init__(self, record, term):
        """
        ctor.

        :param record: Dictionary.
        :param term: Model term.
        :return: None.
        """
        super().__init__(record, term, TermEnum.FUN)

    # flake8: noqa: F841
    @property
    def value(self):
        lhs = self._term.rindex('(') + 1
        rhs = self._term.index(')')
        x_name = self._term[lhs:rhs]
        expression = f'{self._term[0:lhs]}val{self._term[rhs:]}'
        val = self._record[x_name] if x_name in self._record else None
        if pd.isna(val):
            return None

        if 'np.' in expression:
            np = importlib.import_module('numpy')
        v = eval(expression)

        if isinstance(v, np.generic):
            v = np.asscalar(v)
        return v


class InteractionExtractor(object):
    """
    Interaction extractor for interaction effects.
    """

    def __init__(self, record, terms):
        """
        ctor.

        :param record: Dictionary.
        :param terms: Model term (possibly with interaction effects).
        :return: None.
        """
        self._terms = terms
        extractors = [TermEnum.get_extractor(record, term) for term in terms.split(':')]
        values = [e.value for e in extractors]
        values = [v for v in values if pd.notna(v)]

        if len(values) != len(extractors):
            self.__value = None
        else:
            self.__value = reduce(lambda a, b: a * b, values)

    def __repr__(self):
        return f'{self.__class__.__name__}[terms={self._terms}]'

    @property
    def value(self):
        return self.__value
