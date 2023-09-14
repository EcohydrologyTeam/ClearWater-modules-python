import pytest
from clearwater_modules_python.tsm.model import (
    EnergyBudget,
)
from clearwater_modules_python.tsm.constants import (
    DEFAULT_METEOROLOGICAL,
    DEFAULT_TEMPERATURE,
)


@pytest.fixture(scope='module')
def initial_tsm_state(initial_array) -> dict[str, float]:
    """Return initial state values for the model."""
    return {
        't_water_c': initial_array,
        'surface_area': initial_array ** 2,
        'volume': initial_array ** 3,
    }


@pytest.fixture(scope='module')
def tsm_state_variable_names(initial_state_values) -> list[str]:
    """Return the names of the state variables."""
    return list(initial_state_values.keys())


@pytest.fixture(scope='module')
def energy_budget_instance(initial_tsm_state) -> EnergyBudget:
    """Return an instance of the TSM class."""
    return EnergyBudget(
        initial_state_values=initial_tsm_state,
        time_dim='tsm_time_step',
    )


def test_tsm_specific_attributes(energy_budget_instance) -> None:
    """Checks that all TSM variables are present."""
    assert energy_budget_instance.time_dim == 'tsm_time_step'
    assert isinstance(energy_budget_instance.met_parameters, dict)
    assert isinstance(energy_budget_instance.temp_parameters, dict)
    assert energy_budget_instance.met_parameters == DEFAULT_METEOROLOGICAL
    assert energy_budget_instance.temp_parameters == DEFAULT_TEMPERATURE


def test_tsm_variable_sorting(energy_budget_instance) -> None:
    """Checks that we can auto-sort our TSM variable"""
    assert isinstance(energy_budget_instance.computation_order, list)