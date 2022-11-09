# importing the required modules
import PyPDF2
#Create a pdf file object 
pdfFileObj = open('WS_Tracker\Performance_Statements\OCT22.pdf', 'rb')

#Creating a pdf file reader obkect from the pdfgilreader class in the pypdf2 module 
#Create a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)
  
# creating a page object
pageObj = pdfReader.getPage(2)
  
# extracting text from page
print(pageObj.extractText())
# Test Change

#6 Columns // Date : Transaction : Description : Charged : Credit : Balance 







# closing the pdf file object
pdfFileObj.close()
