# algorithms

[![Build
Status](https://travis-ci.org/laurashub/BMI203HW1.svg?branch=master)](https://travis-ci.org/laurashub/BMI203HW1)

Example python project with testing.

## usage

To use the package, first make a new conda environment and activate it

```
conda create -n exampleenv python=3
source activate exampleenv
```

then run

```
conda install --yes --file requirements.txt
```

to install all the dependencies in `requirements.txt`. Then the package's
main function (located in `example/__main__.py`) can be run as follows

```
python -m algorithms
```

## testing

Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.

(modified from https://github.com/ucsf-bmi-203/example/README.md)
