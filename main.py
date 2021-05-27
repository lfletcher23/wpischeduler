import reformat_sheet as rs
import pandas as pd
import generate_objects as gno
import objects

startfile = "Exported_Course_Details.xlsx"
reference_file = "Course_scheduling_abbreviations.xlsx"

df = pd.read_excel(startfile, engine = "openpyxl")
df.dropna(subset=['Meeting Patterns'], inplace = True)
locations_ref = pd.read_excel(reference_file, sheet_name = "Locations", engine = "openpyxl")
depts_ref = pd.read_excel(reference_file, sheet_name = "Dept Codes", engine = "openpyxl")
standard = '<?xml version="1.0" encoding="UTF-8"?> <schedb xmlns="https://scheduler.wpi.edu" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://scheduler.wpi.edu schedb.xsd" generated="MON APR 18 22:00:00 2016" minutes-per-block="30">'

formatted = rs.reformat_sheet(df)
formatted.to_excel("Formatted_527_315.xlsx")
depts_dict = gno.make_dept_objects_dict(depts_ref)
updated_dict = gno.populate_courses(formatted, depts_dict)

file1 = open("courses_formatted_527_315.txt","w")
file1.write(standard)
file1.write("\n")
for key in updated_dict.keys():
    department = updated_dict[key]
    test_json = department.json_format()
    file1.write(test_json)
    file1.write("\n")
    file1.write("\n")
    file1.write("\n")

# department = updated_dict["BUS"]
# test_json = department.json_format()
# file1.write(test_json)
