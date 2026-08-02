import pytest

from econtools.stats import demean, mean, variance


def test_mean():
    assert mean([1, 2, 3]) == 2.0


def test_mean_one_element():
    assert mean([2]) == 2.0


def test_demean_same_length():
    values = [1, 2, 3, 4, 5, 6, 7]
    result = demean(values, mean(values))
    assert len(result) == len(values)


def test_demean_mean_zero():
    values = [1, 2, 3, 4, 5, 6, 7]
    result = demean(values, mean(values))
    assert mean(result) == pytest.approx(0.0)


def test_variance():
    assert variance([1, 2, 3, 4, 5]) == pytest.approx(2.0)


def test_variance_zero():
    assert variance([2, 2, 2]) == pytest.approx(0.0)
