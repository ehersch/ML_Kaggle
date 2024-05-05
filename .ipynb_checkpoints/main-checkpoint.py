import numpy

numpy.loadtxt(
    open(
        "data/train.csv",
    ),
    delimiter=",",
    skiprows=1,
)
