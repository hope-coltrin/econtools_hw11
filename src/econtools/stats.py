def mean(values: list[float]) -> float:
    """Mean of a list of numbers."""
    total = 0

    for value in values:
        total += value

    return total / len(values)


def demean(values: list[float], mean_value: float) -> list[float]:
    """List with the mean subtracted from each value."""
    return [value - mean_value for value in values]


def variance(values: list[float]) -> float:
    """Population variance of a list of numbers."""
    mean_value = mean(values)
    deviations = demean(values, mean_value)

    sum_of_squares = 0

    for value in deviations:
        sum_of_squares += value * value

    return sum_of_squares / len(deviations)
