

import fitz  # PyMuPDF

def extract_paragraphs_from_page(page):
    # Extract the text from the page as a list of lines
    text = page.get_text()
    lines = text.split('\n')
    
    paragraphs = []
    paragraph = ""
    
    for line in lines:
        stripped_line = line.strip()
        #stripped_line = line
        if stripped_line:
            if paragraph:
                paragraph += ' ' + stripped_line
            else:
                paragraph = stripped_line
        else:
            if paragraph:
                paragraphs.append(paragraph)
                paragraph = ""
    
    if paragraph:
        paragraphs.append(paragraph)
    
    return paragraphs

def extract_paragraphs_from_pdf(pdf_path):
    paragraphs = []
    # Open the PDF file
    with fitz.open(pdf_path) as doc:
        # Iterate over each page
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            page_paragraphs = extract_paragraphs_from_page(page)
            paragraphs.extend(page_paragraphs)
    
    return paragraphs


#If it's a standalone script execute
if __name__ == "__main__":
    pdf_path = r"C:\Users\fabic\Downloads\TsengFERD21.pdf"
    paragraphs = extract_paragraphs_from_pdf(pdf_path)
    
    #for i, paragraph in enumerate(paragraphs):
        #print(f"Paragraph {i+1}:\n{paragraph}\n")