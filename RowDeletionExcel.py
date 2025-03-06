from openpyxl import load_workbook

# Load the workbook (Replace with a generic file path)
workbook = load_workbook(r'C:\path\to\your\spreadsheet.xlsx')

# Get the active sheet
sheet1 = workbook.active  # You can also specify a sheet by name: workbook['SheetName']

# Delete row 5
sheet1.delete_rows(5)

# Save the modified workbook (Use a generic filename)
workbook.save(r'C:\path\to\your\modified_spreadsheet.xlsx')
