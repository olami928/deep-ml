import numpy as np
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    values, counts = np.unique(samples, return_counts=True )

    x = len(samples)

    predictions = []

    for count in counts:
        predictions.append(count / x)

    return [(value, prediction) for value, prediction in zip(values, predictions)]