import os

import webbrowser

from fpdf import FPDF

from filestack import Client


class PdfReport:
    """
    Generates a Pdf file that contains data about the flatmates, such as their names, their due amounts and
    the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generates(self, flatmates: dict, period: str) -> None:
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image('files/house.png', w=40, h=40)

        # Add the title

        pdf.set_font(family='Helvetica', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates' Bill", border=0, align='C', ln=1)

        # Add the period label and value

        pdf.set_font(family='Helvetica', size=18, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=300, h=40, txt=f'{period}', border=0, ln=1)

        # Add the flatmates and their payments

        pdf.set_font(family='Helvetica', size=14)
        pdf.cell(w=0, h=20, txt='', border=0, ln=1)
        for nm, am in flatmates.items():
            pdf.cell(w=100, h=25, txt=nm, border=0)
            pdf.cell(w=300, h=25, txt=str(am), border=0, ln=1)

        # Change directory to the files, generate and open the PDF

        if not os.path.exists('reports'):
            os.mkdir('reports')
        os.chdir('reports')
        pdf.output(self.filename)
        webbrowser.open(self.filename)


class FileSharer:
    """
    Uploads the generated PDF file to the cloud and gives a link to the uploaded file. So that user can immediately
    see it in his browser.
    """

    def __init__(self, filepath, api_key=key) -> None:
        self.filepath = filepath
        self.api_key = api_key

    def share(self, mimetype='application/pdf'):
        client = Client(self.api_key)
        store_params = {'mimetype': mimetype}
        new_link = client.upload(filepath=self.filepath, store_params=store_params)
        return new_link.url
