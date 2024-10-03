print("--------------|Example_1|--------------")
# Default order
String1 = "{} {} {}".format('menyala', 'kota', 'medanku')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{2} {1} {0}".format('menyala', 'kota', 'medanku')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{m} {k} {c}".format(c='menyala', k='kota', m='medanku')
print("\nPrint String in order of Keywords: ")
print(String1)


print("--------------|Example_2|--------------")
# Formatting of Integers (Binary representation)
String1 = "{0:b}".format(10)
print("\nBinary representation of 10 is ")
print(String1)

# Formatting of Floats (Exponent representation)
String1 = "{0:e}".format(6062006.6458)
print("\nExponent representation of 6062006.6458 is ")
print(String1)

# Rounding off Floats
String1 = "{0:.2f}".format(3/4)
print("\ntiga per empat adalah : ")
print(String1)

print("--------------|Example_3|--------------")
# String alignment
String1 = "|{:<12}|{:^12}|".format('Kota', 'medan')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# Aligning with additional spaces
String1 = "\n{0:^16} founded in {1:<4}!".format("Kota medan", 1590)
print(String1)


print("--------------|Example_4|--------------")
# Old Style Formatting of Floats
Integer1 = 10.082006
print("Formatting in 3.2f format: ")
print('Nilai dari Integer1 adalah %3.2f' % Integer1)

print("\nFormatting in 3.4f format: ")
print('Nilai dari Integer1 adalah %3.4f' % Integer1)