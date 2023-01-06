import webbrowser, os

from fpdf import FPDF
from filestack import Client

class PdfReport(FPDF):
    """
    Creates a Pdf file that contains data about
    flatmates names, due amount and staying period
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add Icon
        pdf.image("./files/house-icon.png",
                w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80,
                txt="Flatmates Bill",
                border=0,
                align="C",
                ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40,
                txt="Period: ",
                border=0)
        pdf.cell(w=150, h=40,
                txt="March 2022", align="R",
                border=0, ln=1)

        # Insert name and due amount of first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25,
                txt=flatmate1.name,
                border=0)
        pdf.cell(w=150, h=25,
                txt=str(flatmate1.pays(bill, flatmate2)) + " EUR",
                border=0, align="R", ln=1)

        # Insert name and due amount of second flatmate
        pdf.cell(w=100, h=25,
                txt=flatmate2.name,
                border=0)
        pdf.cell(w=150, h=25,
                txt=str(flatmate2.pays(bill, flatmate1)) + " EUR",
                border=0, align="R", ln=1)

        pdf.output(self.filename)
        
        #? Opens in default system pdf application
        # webbrowser.open(f"file://{os.path.abspath(self.filename)}")
        
        # Opens in Chrome
        chrome_dir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(using=chrome_dir).open(f"file://{os.path.abspath(self.filename)}")
        

class FileSharer:
    """
    Shares a file on filestack
    """
    def __init__(self, filepath, api_key="A5EPfwUjQRer32SVAJcbxz"):
        self.filepath = filepath
        self.api_key = api_key
    
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
        