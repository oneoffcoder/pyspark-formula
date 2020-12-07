import random
from random import choice

import numpy as np
import pandas as pd
from pyspark.sql import SparkSession

from ydot.spark import smatrices

random.seed(37)
np.random.seed(37)


def get_spark_dataframe(spark):
    n = 100
    data = {
        'a': [choice(['left', 'right']) for _ in range(n)],
        'b': [choice(['high', 'mid', 'low']) for _ in range(n)],
        'x1': np.random.normal(20, 1, n),
        'x2': np.random.normal(3, 1, n),
        'y': [choice([1.0, 0.0]) for _ in range(n)]
    }
    pdf = pd.DataFrame(data)

    sdf = spark.createDataFrame(pdf)
    return sdf


if __name__ == '__main__':
    try:
        spark = (SparkSession.builder
                 .master('local[4]')
                 .appName('local-testing-pyspark')
                 .getOrCreate())
        sdf = get_spark_dataframe(spark)

        formulas = [
            {
                'f': 'y ~ np.sin(x1) + np.cos(x2) + a + b',
                'o': 'transformed-continuous.csv'
            },
            {
                'f': 'y ~ x1*x2',
                'o': 'star-con-interaction.csv'
            },
            {
                'f': 'y ~ a*b',
                'o': 'star-cat-interaction.csv'
            },
            {
                'f': 'y ~ x1:x2',
                'o': 'colon-con-interaction.csv'
            },
            {
                'f': 'y ~ a:b',
                'o': 'colon-cat-interaction.csv'
            },
            {
                'f': 'y ~ (x1 + x2) / (a + b)',
                'o': 'divide-interaction.csv'
            },
            {
                'f': 'y ~ x1 + x2 + a - 1',
                'o': 'no-intercept.csv'
            }
        ]

        for item in formulas:
            f = item['f']
            o = item['o']

            y, X = smatrices(f, sdf)
            y = y.toPandas()
            X = X.toPandas()

            X.head(5).to_csv(o, index=False)

            s = f"""
            .. csv-table:: {f}
               :file: _code/{o}
               :header-rows: 1
            """
            print(s.strip())
    except Exception as e:
        print(e)
    finally:
        try:
            spark.stop()
            print('closed spark')
        except Exception as e:
            print(e)
