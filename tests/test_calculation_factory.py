import pytest

from app.schemas import CalculationType
from app.services.calculation_factory import CalculationFactory


@pytest.mark.parametrize(
    "a,b,calculation_type,expected",
    [
        (5, 3, CalculationType.ADD, 8),
        (10, 4, CalculationType.SUBTRACT, 6),
        (6, 7, CalculationType.MULTIPLY, 42),
        (20, 5, CalculationType.DIVIDE, 4),
    ],
)
def test_calculation_factory_operations(
    a,
    b,
    calculation_type,
    expected,
):
    result = CalculationFactory.calculate(
        a,
        b,
        calculation_type,
    )

    assert result == expected


def test_calculation_factory_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        CalculationFactory.calculate(
            10,
            0,
            CalculationType.DIVIDE,
        )