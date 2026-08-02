def mean(values: list[float]) -> float:
    """Return the mean of a list of numbers that was input."""
    total = 0

    for value in values:
        total += value

    return total / len(values)


def demean(values: list[float], mean_value: float) -> list[float]:
    """Return a list with the mean subtracted from each value of the list that was input."""
    return [value - mean_value for value in values]


def variance(values: list[float]) -> float:
    """Return the population variance (calulated with mean and demean) of a list of numbers that was input."""
    mean_value = mean(values)
    deviations = demean(values, mean_value)

    sum_of_squares = 0

    for value in deviations:
        sum_of_squares += value * value

    return sum_of_squares / len(deviations)
