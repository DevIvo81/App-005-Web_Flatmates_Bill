import os

from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

os.system("cls")

# Main program

amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? i.e. December 2020: ")

name_1 = input("\nWhat is your name?: ")
days_in_house_1 = int(input(f"How many days did {name_1} stay?: "))

name_2 = input("\nWhat is others name?: ")
days_in_house_2 = int(input(f"How many days did {name_2} stay?: "))


the_bill = Bill(amount, period)
flatmate_1 = Flatmate(name_1, days_in_house_1)
flatmate_2 = Flatmate(name_2, days_in_house_2)

print()
print(f"\n{name_1} pays: {flatmate_1.pays(the_bill, flatmate_2)}")
print()
print(f"{name_2} pays: {flatmate_2.pays(the_bill, flatmate_1)}")
print()

pdf_report = PdfReport(filename="./files/bill.pdf")
pdf_report.generate(flatmate_1, flatmate_2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
