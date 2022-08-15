# datels

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/datels?style=plastic)](https://github.com/joe-yama/datels) [![PyPI - License](https://img.shields.io/pypi/l/datels?style=plastic)](https://github.com/joe-yama/datels) [![PyPI](https://img.shields.io/pypi/v/datels?style=plastic)](https://pypi.org/project/datels/) [![codecov](https://codecov.io/gh/joe-yama/datels/branch/main/graph/badge.svg?token=RCQSYF637E)](https://codecov.io/gh/joe-yama/datels)

`datels` is a Python-based CLI tool to list sequence of dates.

## Installation

```sh
pip install datels
```

## Basic Usage

```sh
$ datels 1994-03-07 1994-03-10
1994/03/07
1994/03/08
1994/03/09
1994/03/10
```

To specify date format:

```sh
# to specify separate charactor
$ datels 1994-03-07 1994-03-10 --sep="-"
1994-03-07
1994-03-08
1994-03-09
1994-03-10
```

```sh
# to specify formatting
$ datels 1994-03-07 1994-03-10 --format "%m/%d/%Y"
03/07/1994
03/08/1994
03/09/1994
03/10/1994
```

See [strftime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) for more information.

To specify date boundaries:

```bash
$ datels 1994-03-07 1994-03-10 --inclusive "both"
1994/03/07
1994/03/08
1994/03/09
1994/03/10

$ datels 1994-03-07 1994-03-10 --inclusive "left"
1994/03/07
1994/03/08
1994/03/09

$ datels 1994-03-07 1994-03-10 --inclusive "right"
1994/03/08
1994/03/09
1994/03/10
```

## Examples

## Download daily partitioned objects from AmazonS3

```bash
#!bin/bash
for DATE in $(datels ${START_DATE} ${END_DATE} --sep "/")
do
  echo "Downloading data of ${DATE}"
  aws s3 cp --recursive s3://your-bucket/dailydata/ . --exclude "*" --include "${DATE}/*"
done
```

## Generate list of dates in Python scripts

```bash
$ python
>>> from datels import list_dates
>>> dates = list_dates("1994-03-07", "1994-03-10", sep="-", inclusive="both")
>>> dates
['1994-03-07', '1994-03-08', '1994-03-09', '1994-03-10']
>>> # list_dates retuens list of string
>>> type(dates)
<class 'list'>
>>> type(dates[0])
<class 'str'>
```
