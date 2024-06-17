import pandas as pd
import pytest

from adoption_model.adoption_model import get_total_cost


# Test data setup can be done using fixtures in pytest
@pytest.fixture
def test_data():
    data = {
        'postcode_df': pd.DataFrame({'postcode': [1000, 2000], 'state': ['NSW', 'VIC']}),
        'capital_costs_by_state_df': pd.DataFrame({
            'state': ['NSW', 'VIC'],
            'solar_cost_per_kW': [1000, 900],
            'battery_only_cost_per_kW': [400, 300],
            'battery_BOP_cost_per_kW': [100, 80],
            'meter_cost': [100, 90],
            'solar_subsidy': [50, 40],
            'battery_subsidy': [20, 15]
        }),
        'cer_installations_df': pd.DataFrame({
            'postcode': [1000, 2000],
            'state': ['NSW', 'VIC'],
            'solar_kW': [5, 6],
            'battery_kW': [1, 2],
            'battery_kWh': [10, 20]
        })
    }
    return data

# Use the fixture by specifying it as an argument to the test function
def test_get_total_cost(test_data):
    total_cost = get_total_cost(test_data['postcode_df'], test_data['capital_costs_by_state_df'], test_data['cer_installations_df'])
    expected_cost = pd.Series([6430, 7635])
    pd.testing.assert_series_equal(total_cost, expected_cost, check_names=False)
