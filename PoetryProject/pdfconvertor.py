
import pdfkit

def convert_html_to_pdf(html_file_path, pdf_file_path):
    try:
        pdfkit.from_file(html_file_path, pdf_file_path)
        print(f"PDF file saved at: {pdf_file_path}")
    except Exception as e:
        print(f"Error converting HTML to PDF: {e}")

if __name__ == "__main__":
    html_file_path = './invoice_template_domonic.html' # Replace with the actual path to your HTML file
    pdf_file_path = './invoice_template_domonic.pdf'  # Replace with the desired path for the output PDF file
    
    convert_html_to_pdf(html_file_path, pdf_file_path)
