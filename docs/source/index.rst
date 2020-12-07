.. meta::
   :description: R-like formulas for Spark Dataframes.
   :keywords: statistics, pyspark, formula, patsy, spark, dataframe, regression, classification, data, machine learning, artificial intelligence
   :robots: index, follow
   :abstract: A Python API to produce PySpark dataframe models from R-like formula expressions.
   :author: Jee Vang, Ph.D.
   :contact: g@oneoffcoder.com
   :copyright: One-Off Coder
   :content: global
   :generator: Sphinx
   :language: English
   :rating: general
   :reply-to: info@oneoffcoder.com
   :web_author: Jee Vang, Ph.D.
   :revisit-after: 1 days

.. ydot documentation master file, created by
   sphinx-quickstart on Sun Dec  6 17:42:42 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ydot
====

.. image:: _static/images/logo.png
   :alt: ydot logo.

``ydot`` is a Python API to produce PySpark dataframe models from R-like formula expressions. This project is based on `patsy <https://patsy.readthedocs.io/en/latest/index.html>`_ :cite:`2020:patsy`. As a quickstart, let's say you have a Spark dataframe with data as follows.

.. csv-table:: Dummy Data in a Spark Dataframe
   :file: _code/data.csv
   :header-rows: 1

Now, let's say you want to model this dataset as follows.

- ``y ~ x_1 + x_2 + a + b``

Then all you have to do is use the ``smatrices()`` function.

.. code-block:: python
   :linenos:

   from ydot.spark import smatrices

   formula = 'y ~ x1 + x2 + a + b'
   y, X = smatrices(formula, sdf)

Observe that ``y`` and ``X`` will be Spark dataframes as specified by the formula. Here's a more interesting example where you want a model specified up to all two-way interactions.

- ``y ~ (x1 + x2 + a + b)**2``

Then you could issue the code as below.

.. code-block:: python
   :linenos:

   from ydot.spark import smatrices

   formula = 'y ~ (x1 + x2 + a + b)**2'
   y, X = smatrices(formula, sdf)

Your resulting ``X`` Spark dataframe will look like the following.

.. csv-table:: Dummy Data Transformed by Formula
   :file: _code/two-way-interactions.csv
   :header-rows: 1

In general, what you get with ``patsy`` is what you get with ``ydot``, however, there are exceptions. For example, the builtin functions such as ``standardize()`` and ``center()`` available with ``patsy`` will not work against Spark dataframes. Additionally, patsy allows for custom transforms, but such transforms (or user defined functions) must be visible. For now, only numpy-based transformed are allowed against continuous variables (or numeric columns).

.. toctree::
   :maxdepth: 2
   :caption: Contents

   quickstart
   zzz-bib

.. toctree::
   :maxdepth: 2
   :caption: API Documentation

   modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

About
=====

.. image:: _static/images/ooc-logo.png
   :alt: One-Off Coder logo.

One-Off Coder is an educational, service and product company. Please visit us online to discover how we may help you achieve life-long success in your personal coding career or with your company's business goals and objectives.

- |Website_Link|
- |Facebook_Link|
- |Twitter_Link|
- |Instagram_Link|
- |YouTube_Link|
- |LinkedIn_Link|

.. |Website_Link| raw:: html

   <a href="https://www.oneoffcoder.com" target="_blank">Website</a>

.. |Facebook_Link| raw:: html

   <a href="https://www.facebook.com/One-Off-Coder-309817926496801/" target="_blank">Facebook</a>

.. |Twitter_Link| raw:: html

   <a href="https://twitter.com/oneoffcoder" target="_blank">Twitter</a>

.. |Instagram_Link| raw:: html

   <a href="https://www.instagram.com/oneoffcoder/" target="_blank">Instagram</a>

.. |YouTube_Link| raw:: html

   <a href="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ" target="_blank">YouTube</a>

.. |LinkedIn_Link| raw:: html

   <a href="https://www.linkedin.com/company/one-off-coder/" target="_blank">LinkedIn</a>

Copyright
=========

Documentation
-------------

.. raw:: html

    <embed>
    This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0 International License</a> by <a href="https://www.oneoffcoder.com" target="_blank">One-Off Coder</a>.
    <br />
    <br />
    <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
        <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" />
    </a>
    <br />
    <br />
    </embed>

Software
--------

::

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

Art
---

::

    Copyright 2020 Daytchia Vang

Citation
========

::

    @misc{oneoffcoder_ydot_2020,
    title={ydot, R-like formulas for Spark Dataframes},
    url={https://github.com/oneoffcoder/pyspark-formula},
    author={Jee Vang},
    year={2020},
    month={Dec}}

Author
======

Jee Vang, Ph.D.

- |Patreon_Link|

.. |Patreon_Link| raw:: html

   <a href="https://www.patreon.com/vangj" target="_blank">Patreon</a>: support is appreciated

Help
====

- |Source_Link|
- |Gitter_Link|

.. |Source_Link| raw:: html

   <a href="https://github.com/oneoffcoder/pyspark-formula" target="_blank">GitHub</a>: source code

.. |Gitter_Link| raw:: html

   <a href="https://gitter.im/dataflava/ydot" target="_blank">Gitter</a>: chat