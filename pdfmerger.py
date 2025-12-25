import PyPDF2 as pypdf

pdfs = [
    '/Users/amritkumaryadav/Desktop/New/Devlopment in Python/PDFMerger/Sample_1.pdf',
    '/Users/amritkumaryadav/Desktop/New/Devlopment in Python/PDFMerger/Sample_2.pdf',
    '/Users/amritkumaryadav/Desktop/New/Devlopment in Python/PDFMerger/Sample_3.pdf'
]

merger = pypdf.PdfMerger()

for pdf in pdfs:
    with open(pdf, 'rb') as pdfFile:
        merger.append(pdfFile)

merger.write("merged-pdf.pdf")
merger.close()
