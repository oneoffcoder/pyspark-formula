from itertools import product
import pandas as pd
from patsy.highlevel import dmatrices


def get_profile(sdf):
    """
    Gets the field profiles of the specified Spark dataframe.

    :param sdf: Spark dataframe.
    :return: Dictionary.
    """
    dtypes = {k: v for k, v in sdf.dtypes}
    cat_types = sdf.rdd \
        .map(lambda r: r.asDict()) \
        .flatMap(lambda r: [((k, r[k]), 1) for k, v in dtypes.items() if v == 'string']) \
        .reduceByKey(lambda a, b: a + b) \
        .map(lambda tup: (tup[0][0], {tup[0][1]: tup[1]})) \
        .reduceByKey(lambda a, b: {**a, **b}) \
        .map(lambda tup: (tup[0], [(k, v) for k, v in tup[1].items()])) \
        .map(lambda tup: (tup[0], sorted(tup[1], key=lambda t: (t[1], t[0]), reverse=True))) \
        .map(lambda tup: (tup[0], [t[0] for t in tup[1]])) \
        .collect()
    cat_types = {tup[0]: tup[1] for tup in cat_types}
    con_types = {k: [1.0] for k, v in dtypes.items() if v != 'string'}
    all_types = {**cat_types, **con_types}
    return all_types


def get_columns(formula, sdf, profile=None):
    """
    Gets the expanded columns of the specified Spark dataframe using the specified formula.

    :param formula: Formula (R-like, based on patsy).
    :param sdf: Spark dataframe.
    :param profile: Profile. Default is `None` and profile will be determined empirically.
    :return: Tuple of columns for y, X.
    """
    if profile is None:
        profile = get_profile(sdf)

    data = product(*(v for _, v in profile.items()))
    columns = [k for k, _ in profile.items()]
    df = pd.DataFrame(data, columns=columns)
    y, X = dmatrices(formula, df, return_type='dataframe')

    return list(y), list(X)


def smatrices(formula, sdf, profile=None):
    # columns = get_columns(formula, sdf, profile=profile)
    raise NotImplementedError()
