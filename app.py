#IMPORTED STUFF
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('dtrees.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        #COUNTRY 

        Country=request.form['Country']
        if(Country=='Belarus'):
            Country = 0
        elif(Country=='Canada'):
            Country = 1
        elif(Country=='Denmark'):
            Country = 2
        elif(Country=='Estonia'):
            Country = 3
        elif(Country=='Finland'):
            Country = 4
        elif(Country=='France'):
            Country = 5
        elif(Country=='Germany'):
            Country = 6
        elif(Country=='Great Britain'):
            Country = 7
        elif(Country=='Latvia'):
            Country = 8
        elif(Country=='Lithuania'):
            Country = 9
        elif(Country=='Morocco'):
            Country = 10
        elif(Country=='Netherlands'):
            Country = 11
        elif(Country=='Nigeria'):
            Country = 12
        elif(Country=='Norway'):
            Country = 13
        elif(Country=='Russia'):
            Country = 14
        elif(Country=='Sweden'):
            Country = 15

        #SEX

        Sex=request.form['Sex']
        if(Sex=='M'):
            Sex = 1
        else:
            Sex = 0

        #AGE

        Age = int(request.form['Age'])

        #CATEGORY

        Category=request.form['Category']
        if(Category=='P'):
            Category = 1
        else:
            Category = 0  


        #PREDICTION

        preds = model.predict([[Country, Sex, Age, Category]])
        output = preds
        
        if output<0:
            return render_template('index.html',prediction_texts="We Ran into an error.")
        else:
            if output==0:
                return render_template('index.html',prediction_text="Verdict: Death.\n You did NOT survive the MS Estonia Disaster.")
            elif output==1:
                return render_template('index.html',prediction_text="Verdict: Congratulations! You survived the MS Estonia Disaster.")
        
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
   