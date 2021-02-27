def decreased_sum(x, y, d):
    assert isinstance(x, (int, float))
    assert isinstance(y, (int, float))
    assert isinstance(d, (int, float))
    return (x + y - d)


def space_to_underscore(s):
    assert isinstance(s, str), "s must be a string"
    return s.replace(" ", "_")
