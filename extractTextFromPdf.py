import PyPDF2

def extract(pdf, path , pagess ):
    # pages :> arrayy contains the the numbers of the pages that you wanna extract him
    # if you wanna extract all the pages put range(N) , N is the number of the pages
    with open(pdf, 'rb') as file:
        r = PyPDF2.PdfFileReader(file)
        pages = r.numPages
        text = ""

        for page in range(pages):
            page_text = r.getPage(page)
            text += page_text.extractText()

    with open(path, 'w', encoding='utf-8') as output_file:
        text = text.replace("https://en.wikipedia.org/wiki/OCP_Group", "")
        text = text.replace("OCP Group - Wikipedia", "")
        text = text.replace("6/11/23, 2:17 PM", "")
        output_file.write(text)

# Example usage:
pdf_file_path = 'docs/OCP Group.pdf'
output_txt_path = 'docs/output2.txt'
arr = [5,6,7,8,9,10]
extract(pdf_file_path, output_txt_path,arr )
