import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb')) # read and open the PDF to process 
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb')) # read and open the watermark PDF
output = PyPDF2.PdfFileWriter() # write the output and combine the PDFs

# loop through the pages and add the watermark
for i in range(template.getNumPages()): # loop through the range number of pages the template has
    page = template.getPage(i) # page object - get each page
    page.mergePage(watermark.getPage(0)) # get the one watermark page and merge the watermark onto the page object
    output.addPage(page) # add the merged page

    with open('watermarked_output.pdf', 'wb') as file: # write the watermarked output
        output.write(file)
