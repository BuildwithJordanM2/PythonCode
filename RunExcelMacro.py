import win32com.client

# Create an instance of Excel
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = False  # Set to True if you want to see Excel

# Open the workbook (Replace with a generic path)
workbook = excel.Workbooks.Open(r'C:\path\to\your\file.xlsx')

# Run the macro (Replace with a generic macro name)
excel.Application.Run('PERSONAL.XLSB!YourMacroName')

# Save and close
workbook.Save()
workbook.Close()

# Quit Excel
excel.Quit()
