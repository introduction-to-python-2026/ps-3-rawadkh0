def approximate_pi(n_terms):
    total = 0.0
    for i in range(n_terms):
        total += ((-1) ** i) / (2 * i + 1)
    return 4 * total
