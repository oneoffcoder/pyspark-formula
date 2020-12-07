import random
from random import choice

import numpy as np
import pandas as pd
from pyspark.sql import SparkSession

from pyspafo.spark import smatrices

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

        y, X = smatrices('y ~ (x1 + x2 + a + b)**2', sdf)
        y = y.toPandas()
        X = X.toPandas()

        print(X.head(10))
        X.head(10).to_csv('two-way-interactions.csv', index=False)
    except Exception as e:
        print(e)
    finally:
        try:
            spark.stop()
            print('closed spark')
        except Exception as e:
            print(e)
