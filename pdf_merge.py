from PyPDF2 import PdfFileMerger
import os

#Python 3.6
#Merges all the PDF files in a folder to a single PDF file, in a new folder. New folder is named "merged".
pdfs = [a for a in os.listdir() if a.endswith(".pdf")]

print (pdfs)
print ('The merging order is going to be as stated above,'
       ' the output PDF in going to be in the "merged" folder, press ENTER to continue')
input()

merger = PdfFileMerger(strict=False)

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

try:
    os.remove("merged/OUTPUT.pdf")
except:
    pass

try:
    os.makedirs('merged')
except:
    pass

with open('merged/OUTPUT.pdf', 'wb') as fout:
    merger.write(fout)

print ('Success!')