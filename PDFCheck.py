from pypdf import PdfReader

bookPath = "/Users/jru/Data/"

bookFile = "Moon Ohio.pdf"

fullPath = bookPath+bookFile

# creating a pdf reader object
reader = PdfReader(fullPath)

# printing number of pages in pdf file
print(len(reader.pages))


