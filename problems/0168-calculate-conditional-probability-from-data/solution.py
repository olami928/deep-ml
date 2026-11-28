def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here

    total_x = 0
    matching = 0

    for a, b in data:
      if a == x:
        total_x += 1

        if b == y:
          matching += 1

    if total_x == 0:
      return 0

    else:
      return round(matching / total_x, 4)
