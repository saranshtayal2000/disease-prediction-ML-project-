from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np
################################

 






















#########################################################
x = True
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    title = 'Disease Predictor'
    return render_template('index.html', title=title)

@app.route("/cancer")
def cancer():
    return render_template("cancer.html")

def ValuePredictor1(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==30):
        loaded_model = joblib.load(r'C:/Users/SARANSH TAYAL/Desktop/health web app/cancer/cancer_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #cancer
        if(len(to_predict_list)==30):
            result = ValuePredictor1(to_predict_list,30)
            
        if(len(to_predict_list)==8):
            result = ValuePredictor2(to_predict_list,8)
            
        if(len(to_predict_list)==7 and x==True):
            result = ValuePredictor3(to_predict_list,7)
            
        if(len(to_predict_list)==7 and x==False):
            result = ValuePredictor4(to_predict_list,7)
            
        if(len(to_predict_list)==10):
            result = ValuePredictor5(to_predict_list,10)
    if(int(result)==1):
        prediction = "Sorry, you have chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return(render_template("result.html", prediction_text=prediction))

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

def ValuePredictor2(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==8):
        loaded_model = joblib.load(r'C:/Users/SARANSH TAYAL/Desktop/health web app/diabetes/diabetes_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]



@app.route("/kidney")
def kidney():
    x=True
    return render_template("kidney.html")

def ValuePredictor3(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load(r'C:/Users/SARANSH TAYAL/Desktop/health web app/health web app/kidney_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/heart")
def heart():
    x=False
    return render_template("heart.html")

def ValuePredictor4(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load(r'C:/Users/SARANSH TAYAL/Desktop/health web app/heart/heart_model2.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/liver")
def liver():
    return render_template("liver.html")

def ValuePredictor5(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==10):
        loaded_model = joblib.load(r'C:/Users/SARANSH TAYAL/Desktop/health web app/liver/liver_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

###############################################

    

if __name__ == "__main__":
    app.run(debug=False)
