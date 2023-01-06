# Flatmates Bill:

Description:
 - An *app* that gets as input the *amount* of a *bill* for particular period and the days that each of flatmates stayed in the house and returns how much each has to pay.
 - It generates a PDF report stating the names of the flatmates, the period, and how much each has to pay. 

Objects:
    Bill:
        amount
        period
    
    Flatmate:
        name
        days_in_house
        pays(bill)
    
    PdfReport:
        filename
        generate(flatmate1, flatmate2, bill)