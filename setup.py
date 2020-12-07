from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_desc = fh.read()

setup(
    name='ydot',
    version='0.0.5',
    author='Jee Vang',
    author_email='vangjee@gmail.com',
    packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
    description='R-like formulas for Spark Dataframes',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/oneoffcoder/pyspark-formula',
    keywords=' '.join(
        ['statistics', 'pyspark', 'formula', 'patsy', 'spark',
         'dataframe', 'regression', 'classification', 'data',
         'machine learning', 'artificial intelligence']),
    install_requires=['scipy', 'numpy', 'pandas', 'scikit-learn', 'pyspark', 'patsy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Development Status :: 5 - Production/Stable'
    ],
    include_package_data=True,
    test_suite='nose.collector'
)
