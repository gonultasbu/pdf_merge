from pikepdf import Pdf
import os
from natsort import natsorted

#Python 3.6.12
#Merges all the PDF files in a folder to a single PDF file, in a new folder. New folder is named "merged".
files = natsorted([a for a in os.listdir() if a.endswith(".pdf")])
files.sort()

print (files)
print ('The merging order is going to be as stated above,'
       ' the output PDF in going to be in the "merged" folder, press ENTER to continue')
input()

pdf = Pdf.new()

for file in files:
    src = Pdf.open(file)
    pdf.pages.extend(src.pages)

try:
    os.remove("merged/OUTPUT.pdf")
except:
    pass

try:
    os.makedirs('merged')
except:
    pass

pdf.save('merged/OUTPUT.pdf')


print ('Success!')