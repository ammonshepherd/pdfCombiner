# PDF COMBINER

A simple script to merge a bunch of PDF files into one.

Given a directory, this program will find all of the PDF files in that
directory and combine them into one PDF file.

If no arguments are given to the command, then it finds all PDF files in the
current directory and combines them into one PDF file.

If no name is given, then it combines all PDFs into a file name MergedFile.pdf

# Requirements
- Python >= 2.7

You will need to have the following Python modules installed

- pdfrw
    - `pip install pdfrw`
    - https://pypi.org/project/pdfrw/
- natsort
    - `pip install natsort`
    - https://pypi.org/project/natsort/

# Usage

To be run on the command line. 

- Find all PDF files in current directory and combine them into one file named combinedFile.pdf
  - `python pdfcombiner.py`

- Create a combined PDF named Gertrude.pdf with all of the files in the current directory.
    - `python pdfcombiner.py . Gertrude.pdf`

- This will find all of the PDF files in the given directory, and create a combined PDF named combinedPDFs.pdf at the given path.
    - `python pdfcombiner.py /path/to/directory/full/of/pdf/files/ /path/to/filename/of/combinedPDFs.pdf`
