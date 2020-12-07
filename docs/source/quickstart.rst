Quickstart
==========

Basic
-----

The best way to learn ``R``-style formula syntax with ``pyspf`` is to head on over to `patsy <https://patsy.readthedocs.io/en/latest/index.html>`_ :cite:`2020:patsy` and read the documentation. Below, we show very simple code to transform a Spark dataframe into two design matrices (these are also Spark dataframes), ``y`` and ``X``, using a formula that defines a model up to two-way interactions.

.. literalinclude:: _code/demo.py
   :language: python
   :linenos:

More
----

We use the code below to generate the models (data) below.

.. literalinclude:: _code/demo-formulas.py
   :language: python
   :linenos:

You can use ``numpy`` functions against continuous variables.

.. csv-table:: y ~ np.sin(x1) + np.cos(x2) + a + b
   :file: _code/transformed-continuous.csv
   :header-rows: 1

The ``*`` specifies interactions and keeps lower order terms.

.. csv-table:: y ~ x1*x2
   :file: _code/star-con-interaction.csv
   :header-rows: 1

.. csv-table:: y ~ a*b
   :file: _code/star-cat-interaction.csv
   :header-rows: 1

The ``:`` specifies interactions and drops lower order terms.

.. csv-table:: y ~ x1:x2
   :file: _code/colon-con-interaction.csv
   :header-rows: 1

.. csv-table:: y ~ a:b
   :file: _code/colon-cat-interaction.csv
   :header-rows: 1

The ``/`` is **quirky** according to the patsy documentation, but it is shorthand for ``a / b = a + a:b``.

.. csv-table:: y ~ (x1 + x2) / (a + b)
   :file: _code/divide-interaction.csv
   :header-rows: 1

If you need to drop the ``Intercept``, add ``- 1`` at the end. Note that one of the dummy variables for ``a`` is not dropped. This could be a bug with patsy.

.. csv-table:: y ~ x1 + x2 + a - 1
   :file: _code/no-intercept.csv
   :header-rows: 1