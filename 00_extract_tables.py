import pdfplumber

# Open the PDF file
with pdfplumber.open("test.pdf") as pdf:
    # Go through each page
    for page in pdf.pages:
        # Get tables from the current page
        tables = page.extract_table()

        # Print the table data
        print(tables)
