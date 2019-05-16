import argparse
import os
from glob import glob
from pdfrw import PdfWriter
from pdfrw import PdfReader
from natsort import natsorted

VERSION = '0.1'

parser = argparse.ArgumentParser(description="Combine a folder of many PDF files into one big PDF file.")
parser.add_argument('path', nargs='?', default=os.getcwd(), help="The path to a directory full of PDF files")
parser.add_argument('combined', nargs='?', default="combinedFile.pdf", help="The name of the combined PDF file")
parser.add_argument('-V', '--version', help='show program version', action='store_true')
parser.add_argument('-v', '--verbose', help='print out information as it goes', action='store_true')

args = parser.parse_args()


if args.version:
    print("pdfCombiner " + VERSION)

if args.combined:
    combinedFile = args.combined

if args.path:
    path = args.path
    if args.verbose:
        print("Searching {} for PDF files.\n".format(path))

# Generate a list of file names (includes the full path)
fileList = []
for filePath in glob(path + "/*.pdf"):
    if args.verbose:
        print("Found {}".format(filePath))
    fileList.append(filePath)

# sort the list in 'natural' order
sortedFiles = natsorted(fileList)

# loop through the list of PDFs, and add them to a new PDF
outFile = PdfWriter()
for pdf in sortedFiles:
    x = PdfReader(pdf)
    if args.verbose:
        print("Adding {} pages from {} to the combined file.".format(x.numPages, pdf))
    outFile.addpages(x.pages)

outFile.write(combinedFile)

if args.verbose:
    m = PdfReader(combinedFile)
    print("\nCombined file created at {} with a total of {} pages.".format(combinedFile, m.numPages))

