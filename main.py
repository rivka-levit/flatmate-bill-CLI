from flat import Flatmate, Bill
from pdf_gen import PdfReport, FileSharer

# Creates a bill.

amount = float(input('Enter the bill amount: '))
period = input('Enter the period (e.g. December 2022): ')
bill = Bill(amount, period)

# Creates a list of the flatmates that live en the flat.

n = int(input('How many flatmates in the flat? '))
fls = list()
for i in range(1, n+1):
    name = input(f"Enter the {i} flatmate's name: ")
    days = int(input(f"How many days did {name} stay in the flat during the bill period? "))
    fls.append(Flatmate(name, days))

# Prints payment information for all the flatmates.

for k, v in bill.to_pay(fls).items():
    print(f'{k} pays: {v}')

# Generates PDF report for the bill split to all the flatmates.

pdf_report = PdfReport(f'{bill.period.replace(" ", "_")}.pdf')
pdf_report.generates(bill.to_pay(fls), bill.period)

# Uploads the PDF file to the cloud and gives a link to it

share_pdf = FileSharer(pdf_report.filename)
print(share_pdf.share())
