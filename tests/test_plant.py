from plant import Plant
from unittest.mock import patch
import pytest

@pytest.fixture
def mock_input(monkeypatch):
    def mock_input_func(value):
        return value
    monkeypatch.setattr('builtins.input', mock_input_func)

def test_init():
    plant = Plant("Rose", [20, 30])
    assert plant.name == "Rose"
    assert plant.optimal_temp == [20, 30]

def test_str():
    plant = Plant("Sunflower", [25, 35])
    expected_output = "Name: Sunflower. \nOptimal temperature is between 25 and 35 degrees Celsius \nMinimum moisture reading 400"
    assert str(plant) == expected_output

def test_get_name_valid_input():
    with patch('builtins.input', return_value='Sunflower'):
        assert Plant.get_name() == 'Sunflower'

def test_get_temperature_valid_input(monkeypatch):
    with patch('builtins.input', return_value='25'):
        assert Plant.get_temperature("MINIMUM") == 25