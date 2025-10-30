import pickle
import numpy as np
with open("ran_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

def predict_price(input_data):
    data=np.array([input_data])
    predicted_price = loaded_model.predict(data)
    return predicted_price[0]
from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit',methods=['POST'])
def submit():
    input_data=[]
    input_data.append(float(request.form['CRIM']))
    input_data.append(float(request.form['ZN']))
    input_data.append(float(request.form['INDUS']))
    input_data.append(float(request.form['CHAS']))
    input_data.append(float(request.form['NOX']))
    input_data.append(float(request.form['RM']))
    input_data.append(float(request.form['AGE']))
    input_data.append(float(request.form['DIS']))
    input_data.append(float(request.form['RAD']))
    input_data.append(float(request.form['TAX']))
    input_data.append(float(request.form['PTRATIO']))
    input_data.append(float(request.form['B']))
    input_data.append(float(request.form['LSTAT']))
    predicted_price = predict_price(input_data)
    # Convert price to float and ensure it's properly formatted
    price = float(predicted_price)
    return render_template('result.html', price=price)
if __name__=="__main__":
    app.run(debug=True)
