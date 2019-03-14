from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in
                        bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))
    return transformed_rows


def test_equal():
    var = ['A', 'B', 'C', 'D']
    test_values_eq = var
    exp_transformed_cities = [
        ('A', [0, 0, 0, 1]),
        ('B', [0, 0, 1, 0]),
        ('C', [0, 1, 0, 0]),
        ('D', [1, 0, 0, 0])
    ]
    transformed_cities = fit_transform(test_values_eq)
    assert transformed_cities == exp_transformed_cities


def test_not_equal():
    var = ['A', 'B', 'C']
    test_values_not_eq = var
    exp_transformed_cities = [
        ('A', [0, 0, 0]),
        ('B', [0, 0, 0]),
        ('C', [0, 0, 0])
    ]
    transformed_cities = fit_transform(test_values_not_eq)
    assert transformed_cities != exp_transformed_cities


def test_not_in():
    var = ['Detroit', 'Petersburg']
    test_values_not_in = var
    exp_transformed_cities = [
        ('Moscow', [0, 1]),
        ('New York', [1, 0]),
    ]
    transformed_cities = fit_transform(test_values_not_in)
    assert transformed_cities not in exp_transformed_cities


def test_error():
    x = '1'
    assert fit_transform(x)
    with pytest.raises(TypeError):
        fit_transform(int(x))
