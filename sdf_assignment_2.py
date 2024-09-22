"""
Description: This program demonstrates different kinds of data types and collections in Python.
Author: Gaganpreet Kaur
Date: September,21,2024

"""

#SIMPLE DATA TYPES

name = "Gaganpreet"
print(f"value: {name} type: {type(name)}")

is_valid_driving_license = False
print(f"value: {is_valid_driving_license} type: {type(is_valid_driving_license)}")

current_year = 2024
print(f"this year: {current_year} type: {type(current_year)}")

current_year += 1     # Increase the current year by using operation +=
print(f"next year: {current_year} type: {type(current_year)}")

#CALCULATIONS

FEDERAL_TAX_RATE_GST = 0.05         # Constant variable
PROVINCIAL_TAX_RATE_PST = 0.07      # Constant variable 
price_vehicle = 90000.43

changed_rate_gst = FEDERAL_TAX_RATE_GST * price_vehicle 
changed_rate_pst = PROVINCIAL_TAX_RATE_PST * price_vehicle 

total_price = price_vehicle + changed_rate_gst + changed_rate_pst

print(f"Pre-tax value: {price_vehicle} Provincial Tax: {changed_rate_pst} Federal Tax: {changed_rate_gst} Total: {total_price}")

print(f"Pre-tax value: ${round(price_vehicle,2):,} Provincial Tax: ${round(changed_rate_pst,2):,} Federal Tax: ${round(changed_rate_gst,2):,} Total: ${round(total_price,2):,}")


#LISTS

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(list_of_numbers))
print(f"First List: {list_of_numbers}")

list_of_numbers.insert(5,"Gaganpreet")  # Insert name between 5 and 6
print(f"List: {list_of_numbers}")

list_of_numbers.remove(9)               # Remove 9 from the list
print(f"List: {list_of_numbers}")

second_list = ["A","B","C"]
third_list = [list_of_numbers , second_list]
print(f"Final List: {third_list}")

#TUPLES

tuple = ("Manitoba","Alberta","British Columbia","Nova Scotia")
print(type(tuple))
print(f"Tuple values are: {tuple}")


#DICTIONARIES

dictionary_values = {'nickel': 0.05 ,'dime':  0.10,'quarter': 0.25}    # Values in floating point
print(type(dictionary_values))
print(f"Dictionary values are: {dictionary_values}")

dictionary_values['nickel'] =int((dictionary_values['nickel'])*100)
dictionary_values['dime'] = int((dictionary_values['dime'])*100)
dictionary_values['quarter'] =int((dictionary_values['quarter'])*100)

print(f"After modification Dictionary values are: {dictionary_values}")

dictionary_values['Lonnie'] = 100        # Added Lonnie and Toonie
dictionary_values['Tonnie'] = 200
 
print(f"Including Lonnie and Toonie dictionary values are: {dictionary_values}")

#SETS

first_set_values = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(type(first_set_values))
print(f"Set of even values multiple of 2 = {first_set_values}")

second_set_values = {5, 10, 15, 20}
print(f"Set of even values multiple of 5 = {second_set_values}")

third_set_values = first_set_values.union(second_set_values)     # Unique values 
print(f"Set of unique values = {third_set_values}")

fourth_set_values = first_set_values.intersection(second_set_values)     # Common values
print(f"Set of common values = {fourth_set_values}")

fifth_set_values = first_set_values.difference(second_set_values)    # Values that appear in first set
print(f"First Set of difference values = {fifth_set_values}")

sixth_set_values = second_set_values.difference(first_set_values)    # Values that appear in second set
print(f"Second Set of difference values = {sixth_set_values}")
