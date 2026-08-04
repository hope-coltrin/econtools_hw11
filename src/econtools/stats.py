def mean(values: list[float]) -> float:
    """Calculate the mean of a list of numbers.

    Parameters
    values : list[float]
        A list of numeric values.

    Return value
    float
        The average of the values given in the list.
    """
    total = 0

    for value in values:
        total += value

    return total / len(values)


def demean(values: list[float], mean_value: float) -> list[float]:
    """Subtract the mean from each value in a list to center the values around a mean of 0.

    Parameters
    values : list[float]
        A list of numeric values.
    mean_value : float
        The average of the values given in the list.

    Return value
    list[float]
        A new list where the mean has been subtracted from each value.
    """
    return [value - mean_value for value in values]


def variance(values: list[float]) -> float:
    """Calculate the population variance of a list of numbers by subtracting the mean from each value,
    squaring the deviations, and then averaging the squared deviations.

    Parameters
    values : list[float]
        A list of numeric values.

    Return value
    float
        The population variance of the values.
    """
    mean_value = mean(values)
    deviations = demean(values, mean_value)

    sum_of_squares = 0

    for value in deviations:
        sum_of_squares += value * value

    return sum_of_squares / len(deviations)
