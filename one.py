from math import floor

def get_fuel_required(mass: int):
  fuel = floor(mass / 3) - 2
  if fuel <= 0:
    return 0
  return fuel + get_fuel_required(fuel)


if __name__ == '__main__':
  total_fuel = 0
  file = open('fuel.txt')
  for line in file:
    mass = int(line)
    total_fuel += get_fuel_required(mass)
  print("Total Fuel: {}".format(total_fuel))
