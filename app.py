# importing libraries
import numpy as np
import pickle
from flask import Flask,request,render_template


# Global variables 
app = Flask(__name__)
loadedModel=pickle.load(open('mobile.pkl','rb'))
 
#User Defined functions
@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')


@app.route('/prediction' ,methods=['POST'])
def predict():
    brand=request.form['brand']
    model=request.form['model']
    batterypower=request.form['battery_power']
    memory=request.form['memory_space']
    ram=request.form['ram']
    height=request.form['px_height']
    width=request.form['px_width']
    good_bad=request.form['good_bad']

    prediction=loadedModel.predict([[batterypower,memory,height,width,ram]])

    if prediction==[0]:
        prediction="Low Budget Range"
    elif prediction==[1]:
        prediction="Mid Budget Range"
    elif prediction==[2]:
        prediction="High Budget Range "
    else:
        prediction="Flagship "

    # return render_template('index.html',prediction_text='Your Mobile Ranges B/w ${}'.format(prediction))
    return render_template('index.html',output=prediction)
#main Function
if __name__=='__main__':
    app.run(debug=True) 
