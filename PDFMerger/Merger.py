import os
from os import listdir
from os.path import isfile, join
from pyPdf import PdfFileWriter, PdfFileReader

cwd = os.getcwd()
PDFs = []
onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]
count = 0


def append_pdf(input, output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]


output = PdfFileWriter()
PDFs = [s for s in onlyfiles if ".pdf" in s]


# Appending two pdf-pages from two different files
# if any(".pdf" in s for s in onlyfiles):
#     print("found!")
#     PDFs = onlyfiles[count]
#     count = count + 1
for f in PDFs:
    append_pdf(PdfFileReader(open(f, "rb")), output)


# Writing all the collected pages to a file
output.write(open("CombinedPages.pdf", "wb"))
print(PDFs)
print(onlyfiles)
