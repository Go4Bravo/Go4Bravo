import fitz  # PyMuPDF

search_text = "ISBN"

# Open the PDF file
bookPath = "/Users/jru/Data/"
bookFile = "Moon Ohio.pdf"
fullPath = bookPath+bookFile
pdf = fitz.open(fullPath)

# Search for the text "ISBN"

for page_num in range(len(pdf)):
    page = pdf.load_page(page_num)  # Load each page
    text_instances = page.search_for(search_text)
    
    # Print the results
    if text_instances:
        print(f"Found '{search_text}' on page {page_num + 1} at positions:")
        for instance in text_instances:
            print(f"  {instance}")

pdf.close()
