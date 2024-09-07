population = int(input("Number of population >"))

# Calculating the number of toilets
num_toilets = population / 3

# Calculating the daily water usage for old and new toilets
old_water_usage = num_toilets * 15 * 14
new_water_usage = num_toilets * 2 * 14

 # Calculating the water saved
water_saved = old_water_usage - new_water_usage

# Calculating the total cost of replacing the toilets
total_cost = num_toilets * 150

print(f"Water saved: {water_saved} liters/day")
print(f"Total cost of replacing toilets: ${total_cost}")
