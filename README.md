![ydot logo](https://ydot.readthedocs.io/en/latest/_images/logo.png)

# ydot

R-like formulas for Spark Dataframes.

- [Documentation](https://ydot.readthedocs.io/)
- [PyPi](https://pypi.org/project/ydot/) 
- [Gitter](https://gitter.im/dataflava/ydot)

Now you have the expressive power of R-like formulas to produce design matrices for your experimental needs. This API is based off of [patsy](https://patsy.readthedocs.io/en/latest/), but for use with Apache Spark dataframes. Given a Spark dataframe, you can express your design matrices with something that resembles the following.

`y ~ x1 + x2 + (x3 + a + b)**2`

Here's a short and sweet example.

```python
from ydot.spark import smatrices

spark_df = get_a_spark_dataframe()
formula = 'y ~ x1 + x2 + (x3 + a + b)**2'
y, X = smatrices(formula, spark_df)
```

# Software Copyright

```
Copyright 2020 One-Off Coder

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

# Book Copyright

Copyright 2020 One-Off Coder

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) by [One-Off Coder](https://www.oneoffcoder.com).

![Creative Commons Attribution 4.0 International License](https://i.creativecommons.org/l/by/4.0/88x31.png "Creative Commons Attribution 4.0 International License")

# Art Copyright

Copyright 2020 Daytchia Vang

# Citation

```
@misc{oneoffcoder_ydot_2020,
title={ydot, R-like formulas for Spark Dataframes},
url={https://github.com/oneoffcoder/pyspark-formula},
author={Jee Vang},
year={2020},
month={Dec}}
```
