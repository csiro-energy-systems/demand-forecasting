import pandas as pd

def get_payback_period(postcode_df, capital_costs_by_state_df, cer_installations_df):
    """
    Calculate the payback period for the adoption of a new technology.

    Parameters:
    - postcode_df (pandas.DataFrame): DataFrame containing postcode and state information.
    - capital_costs_by_state_df (pandas.DataFrame): DataFrame containing capital costs by state.
    - cer_installations_df (pandas.DataFrame): DataFrame containing installation information.

    Returns:
    - payback_period_yrs (float): The payback period in years.
    """
    total_cost = get_total_cost(postcode_df, capital_costs_by_state_df, cer_installations_df)
    savings_per_year = get_savings_per_year(postcode_df, cer_installations_df)
    payback_period_yrs = total_cost / savings_per_year
    return payback_period_yrs

def get_total_cost(postcode_df, capital_costs_by_state_df, cer_installations_df):
    """
    Calculate the total lifetime cost (capital plus operating less discounts) of 
    the solar plus battery system.

    Parameters:
    - postcode_df (pandas.DataFrame): DataFrame containing postcode and state information.
    - capital_costs_by_state_df (pandas.DataFrame): DataFrame containing capital costs by state.
    - cer_installations_df (pandas.DataFrame): DataFrame containing installation information.

    Returns:
    - total_cost (float): The total lifetime cost of the solar plus battery system.
    """

    # Assuming 'state' is the common column in both DataFrames
    df = postcode_df.merge(capital_costs_by_state_df, on='state', how='left')
    df = df.merge(cer_installations_df, on=['postcode', 'state'], how='left') 

    # Calculate costs
    meter_cost = df['meter_cost']
    solar_cost = df['solar_kW'] * df['solar_cost_per_kW']
    solar_subsidy = df['solar_subsidy']
    battery_cost = df['battery_kW'] * df['battery_only_cost_per_kW'] + df['battery_kWh'] * df['battery_BOP_cost_per_kW']
    battery_subsidy = df['battery_subsidy']

    total_cost = meter_cost + solar_cost + battery_cost - solar_subsidy - battery_subsidy

    return total_cost

def get_savings_per_year(postcode_df, cer_installations_df):
    """
    Calculate the savings per year from the solar plus battery system.

    Parameters:
    - postcode_df (pandas.DataFrame): DataFrame containing postcode and state information.
    - cer_installations_df (pandas.DataFrame): DataFrame containing installation information.

    Returns:
    - savings_per_year (float): The annual savings from the solar plus battery system.
    """
    # Placeholder for actual calculation, assuming some constant savings for demonstration
    savings_per_year = 2000
    return savings_per_year

def create_test_data():
    """
    Create test data to test the functions.

    Returns:
    - postcode_df (pandas.DataFrame): DataFrame containing postcode and state information.
    - capital_costs_by_state_df (pandas.DataFrame): DataFrame containing capital costs by state.
    - cer_installations_df (pandas.DataFrame): DataFrame containing installation information.
    """
    # Postcodes and states used to construct the dataframes
    postcodes = [2000, 2001, 2002, 3000, 3001, 3002, 4000, 4001, 4002]
    states = ['NSW', 'VIC', 'QLD']
    
    # postcode_df: postcode, state
    postcode_df = pd.DataFrame({
        'postcode': postcodes,
        'state': ['NSW', 'NSW', 'NSW', 'VIC', 'VIC', 'VIC', 'QLD', 'QLD', 'QLD']
    })

    # capital_costs_by_state_df: state, solar_cost_per_kW, battery_only_cost_per_kW, battery_BOP_cost_per_kW, meter_cost, solar_subsidy, battery_subsidy
    capital_costs_by_state_df = pd.DataFrame({
        'state': states,
        'solar_cost_per_kW': [1000, 900, 800],
        'battery_only_cost_per_kW': [400, 300, 200],
        'battery_BOP_cost_per_kW': [100, 80, 60],
        'meter_cost': [100, 90, 80],
        'solar_subsidy': [50, 40, 30],
        'battery_subsidy': [20, 15, 10]
    })

    # cer_installations_df: postcode, state, solar_kW, battery_kW, battery_kWh
    cer_installations_df = pd.DataFrame({
        'postcode': postcodes,
        'state': ['NSW', 'NSW', 'NSW', 'VIC', 'VIC', 'VIC', 'QLD', 'QLD', 'QLD'],
        'solar_kW': [5, 6, 7, 8, 9, 10, 11, 12, 13],
        'battery_kW': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'battery_kWh': [10, 20, 30, 40, 50, 60, 70, 80, 90]
    })
    
    return postcode_df, capital_costs_by_state_df, cer_installations_df

if __name__ == "__main__":
    postcode_df, capital_costs_by_state_df, cer_installations_df = create_test_data()
    print(get_payback_period(postcode_df, capital_costs_by_state_df, cer_installations_df))
