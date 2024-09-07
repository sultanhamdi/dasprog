dollar = float(input("Enter the amount in US dollars: "))

conversion_rate = 0.65

# Convert dollars to pounds
pound = dollar * conversion_rate

print(f"{dollar} USD is equal to {pound:.2f} GBP")