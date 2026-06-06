"""""
TODO: my typical blurb
"""""

import pytest

from app.models.airfryer import Airfryer

# this is fixture gives us a reusable same object in out test
# it helps us to avoid re-instantiating the same object
@pytest.fixture(scope="module")

def fryer():
    return Airfryer()

def test_airfryer(fryer):
    assert fryer.fry() == "Chips is frying food"

def test_set_temperature_valid(fryer):
    assert fryer.set_temperature(5) ==  f"Airfrying temperature set to {5} degrees C"


def test_set_temperature_invalid(fryer):
    with pytest.raises(ValueError) as e:
        fryer.set_temperature(3000)
        assert str(e.value) == "Temperature must be between 0 and 100"


def test_calculate_tip(fryer):
    # assert fryer.calculate_tip(5) == 1.2417566953150931
    #
    # assert fryer.calculate_tip(50) == 19.680517330979
    #
    # assert isinstance(fryer.calculate_tip(50), float)

    with pytest.raises(ValueError) as e:
        fryer.calculate_tip(-5)
    assert str(e.value) == "Weight must be between 0 and 100"




