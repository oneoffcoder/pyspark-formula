from enum import IntEnum
from abc import ABC, abstractmethod


class TermEnum(IntEnum):
    CAT = 1
    LVL = 2
    CON = 3
    FUN = 4
    INT = 5

    @staticmethod
    def get_type(record, term):
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
    def __init__(self, record, term, term_type):
        self._record = record
        self._term = term
        self._type = term_type

    @property
    @abstractmethod
    def value(self):
        pass


class CatExtractor(Extractor):

    def __init__(self, record, term):
        super().__init__(record, term, TermEnum.CAT)

    def value(self):
        return None


class LvlExtractor(Extractor):

    def __init__(self, record, term):
        super().__init__(record, term, TermEnum.LVL)

    def value(self):
        return None


class ConExtractor(Extractor):

    def __init__(self, record, term):
        super().__init__(record, term, TermEnum.CON)

    def value(self):
        return self._record[self._term]


class IntExtractor(Extractor):

    def __init__(self, record, term):
        super().__init__(record, term, TermEnum.INT)

    def value(self):
        return 1.0


class FunExtractor(Extractor):

    def __init__(self, record, term):
        super().__init__(record, term, TermEnum.FUN)

    def value(self):
        lhs = self._term.rindex('(') + 1
        rhs = self._term.index(')')
        x_name = self._term[lhs:rhs]
        expression = f'{self._term[0:lhs]}val{self._term[rhs:]}'
        val =
        return None


class ValueExtractor(object):

    def __init__(self, record, terms):
        self.__terms = [TermEnum.get_type(record, term) for term in terms.split(':')]


