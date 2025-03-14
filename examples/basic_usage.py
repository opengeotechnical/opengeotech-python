"""
Basic usage example for the opengeotech package.
"""

from opengeotech import effective_stress

# Example 1: Basic calculation
total_stress = 100  # kPa
pore_water_pressure = 40  # kPa
sigma_prime = effective_stress(total_stress, pore_water_pressure)
print(f"Example 1: Total stress = {total_stress} kPa, Pore water pressure = {pore_water_pressure} kPa")
print(f"          Effective stress = {sigma_prime} kPa")

# Example 2: Negative effective stress (uplift condition)
total_stress = 50  # kPa
pore_water_pressure = 70  # kPa
sigma_prime = effective_stress(total_stress, pore_water_pressure)
print(f"\nExample 2: Total stress = {total_stress} kPa, Pore water pressure = {pore_water_pressure} kPa")
print(f"          Effective stress = {sigma_prime} kPa (uplift condition)")

# Example 3: Zero pore water pressure
total_stress = 100  # kPa
pore_water_pressure = 0  # kPa
sigma_prime = effective_stress(total_stress, pore_water_pressure)
print(f"\nExample 3: Total stress = {total_stress} kPa, Pore water pressure = {pore_water_pressure} kPa")
print(f"          Effective stress = {sigma_prime} kPa") 