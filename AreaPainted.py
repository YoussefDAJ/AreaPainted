# Setting
length_str = input("Please enter your length:\n")
width_str = input("Please enter your width:\n")
coast_str = input("Please enter your cost of the meter:\n")

# Converting
length = float(length_str)
width = float(width_str)
area = length * width
area_str = str(area)
coast = float(coast_str) * area
coast_str2 = str(coast)

# Printing
print("The total area is : " + area_str)
print("Give the guy : $" + coast_str2)
