"""Advent of Code 2019 Day 1: The Tyranny of the Rocket Equation"""

import helper
import math

def calculate_fuel(mass): 
    return math.floor(mass / 3) - 2


def calculate_fuel_recursive(mass):
    fuel = calculate_fuel(mass)
    if fuel > 0:
        return fuel + calculate_fuel_recursive(fuel)
    else:
        return 0


assert calculate_fuel(12) == 2
assert calculate_fuel(14) == 2
assert calculate_fuel(1969) == 654
assert calculate_fuel(100756) == 33583

input_masses = [int(mass) for mass in helper.read_day(1).splitlines()]
print("Fuel requirements (1):", sum(calculate_fuel(m) for m in input_masses))

assert calculate_fuel_recursive(14) == 2
assert calculate_fuel_recursive(1969) == 966
assert calculate_fuel_recursive(100756) == 50346

print("Fuel requirements (2)", sum(calculate_fuel_recursive(m) for m in input_masses))