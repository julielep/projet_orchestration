"""Tests/tests.maths.py
Test les fonctions mathématiques.
"""

import app_api.maths as maths
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 12),
        (20, 2, 22),
        (0, 2, 2),
        (0.1, 0.2, 0.3),  # float
    ],
)
def test_add(a, b, expected):
    assert maths.add(a, b) == pytest.approx(expected)  # approx pour float

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 20),
        (20, 2, 40),
        (0, 2, 0),
    ],
)
def test_multiply(a, b, expected):
    assert maths.multiply(a, b) == expected