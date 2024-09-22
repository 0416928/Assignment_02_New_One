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

#TUPLES

#DICTIONARIES

#SETS

