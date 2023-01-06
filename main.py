from unittest import result
from flask import Flask, render_template, url_for, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flatmates_bill import flat

app = Flask(__name__)

class HomePage(MethodView):
    
    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):
    
    def get(self):
        bill_form = BillForm()
        return render_template(
            "bill_form_page.html",
            bill_form=bill_form
            )
    
    def post(self):
        bill_form = BillForm(request.form)
        
        the_bill = flat.Bill(float(bill_form.amount.data), bill_form.period.data)
        flatmate1 = flat.Flatmate(bill_form.name1.data, float(bill_form.days_in_house1.data))
        flatmate2 = flat.Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))
        
        return render_template("bill_form_page.html",
                            result = True,
                            bill_form=bill_form,
                            name1 = flatmate1.name,
                            amount1 = flatmate1.pays(the_bill, flatmate2),
                            name2 = flatmate2.name,
                            amount2 = flatmate2.pays(the_bill, flatmate1)
                            )


class ResultsPage(MethodView):
    
    def post(self):
        bill_form = BillForm(request.form)
        
        the_bill = flat.Bill(float(bill_form.amount.data), bill_form.period.data)
        flatmate1 = flat.Flatmate(bill_form.name1.data, float(bill_form.days_in_house1.data))
        flatmate2 = flat.Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))
        
        return render_template("results.html",
                            name1 = flatmate1.name,
                            amount1 = flatmate1.pays(the_bill, flatmate2),
                            name2 = flatmate2.name,
                            amount2 = flatmate2.pays(the_bill, flatmate1)
                            )


class BillForm(Form):
    amount = StringField("Bill Amount:\t", default=100)
    period = StringField("Bill Period:\t", default="December 2022")
    
    name1 = StringField("Name:\t", default="Ivo")
    days_in_house1 = StringField("Days in the house: ", default=20)
    
    name2 = StringField("Name:\t", default="Ana")
    days_in_house2 = StringField("Days in the house: ", default=12)
    
    btn_submit = SubmitField("Calculate")
    
    
    

app.add_url_rule('/',
                view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form_page', 
                view_func=BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/results', 
#                 view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)