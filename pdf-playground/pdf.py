import PyPDF2
import sys

inputs = sys.argv[1:]# grab the arguments


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)# merge the looped through PDFs
    merger.write('super.pdf')# combine all PDFs to a new PDF file

pdf_combiner(inputs)


