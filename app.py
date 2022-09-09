from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('flight_fare_rf.pkl', 'rb'))

@app.route('/')
@cross_origin()
def home():
    return render_template('home.html')


@app.route('/predict', methods = ['GET','POST'])
@cross_origin()
def predict():
    if request.method == 'POST':

        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format = '%Y-%m-%dT%H:%M').day)
        Journey_month = int(pd.to_datetime(date_dep, format = '%Y-%m-%dT%H:%M').month)

        Dep_hour = int(pd.to_datetime(date_dep, format = '%Y-%m-%dT%H:%M').hour)
        Dep_mins = int(pd.to_datetime(date_dep, format = '%Y-%m-%dT%H:%M').minute)

        date_arr = request.form["Arrival_Time"]
        Arr_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arr_mins = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

        Duration_hours = abs(Arr_hour - Dep_hour)
        Duration_mins = abs(Arr_mins - Dep_mins)

        Stops = int(request.form["stops"])

        airline=request.form['airline']

        if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
            
        elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        Source = request.form["Source"]
        
        if (Source == 'Delhi'):
            Delhi = 1
            Kolkata = 0
            Mumbai = 0
            Chennai = 0

        elif (Source == 'Kolkata'):
            Delhi = 0
            Kolkata = 1
            Mumbai = 0
            Chennai = 0

        elif (Source == 'Mumbai'):
            Delhi = 0
            Kolkata = 0
            Mumbai = 1
            Chennai = 0

        elif (Source == 'Chennai'):
            Delhi = 0
            Kolkata = 0
            Mumbai = 0
            Chennai = 1

        else:
            Delhi = 0
            Kolkata = 0
            Mumbai = 0
            Chennai = 0

        Source = request.form["Destination"]
        
        if (Source == 'Cochin'):
            Cochin = 1
            Delhi = 0
            New_Delhi = 0
            Hyderabad = 0
            Kolkata = 0
        
        elif (Source == 'Delhi'):
            Cochin = 0
            Delhi = 1
            New_Delhi = 0
            Hyderabad = 0
            Kolkata = 0

        elif (Source == 'New_Delhi'):
            Cochin = 0
            Delhi = 0
            New_Delhi = 1
            Hyderabad = 0
            Kolkata = 0

        elif (Source == 'Hyderabad'):
            Cochin = 0
            Delhi = 0
            New_Delhi = 0
            Hyderabad = 1
            Kolkata = 0

        elif (Source == 'Kolkata'):
            Cochin = 0
            Delhi = 0
            New_Delhi = 0
            Hyderabad = 0
            Kolkata = 1

        else:
            Cochin = 0
            Delhi = 0
            New_Delhi = 0
            Hyderabad = 0
            Kolkata = 0

        prediction = model.predict([[Journey_day, Journey_month, Dep_hour, Dep_mins, Arr_hour,
        Arr_mins, Duration_hours, Duration_mins, Stops, Air_India,
       GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
       Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet,
       Trujet, Vistara, Vistara_Premium_economy, Cochin, Delhi,
       Hyderabad, Kolkata, New_Delhi, Chennai, Delhi, Kolkata,
       Mumbai]])
        output = round(prediction[0],2)
        return render_template('home.html', prediction_text = 'Your Flight fare is Rs {}'.format(output))

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)