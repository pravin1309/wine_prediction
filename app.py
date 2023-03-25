from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("wine.html")

@app.route("/predict",methods=["POST"])
def predict_wine_quality():
    fixedacidity=float(request.form.get("fixedacidity"))
    volatileacidity=float(request.form.get("volatileacidity"))
    citricacid=float(request.form.get("citricacid"))
    residualsugar=float(request.form.get("residualsugar"))
    chlorides=float(request.form.get("chlorides"))
    freesulfurdioxide=float(request.form.get("freesulfurdioxide"))
    totalsulfurdioxide=float(request.form.get("totalsulfurdioxide"))
    density=float(request.form.get("density"))
    pH=float(request.form.get("pH"))
    sulphates=float(request.form.get("sulphates"))
    alcohol=float(request.form.get("alcohol"))

    
    result=model.predict(np.array([[fixedacidity, volatileacidity, citricacid, residualsugar, chlorides, 
       freesulfurdioxide, totalsulfurdioxide, density, pH, sulphates, alcohol]]))
    
    if result[0]==1:
        return "<h1 style='color:green'>Good wine</h1>"
    else:
        return "<h1 style='color:red'>Bad quality of wine</h1>"
     

app.run(host="0.0.0.0", port=8080,debug=False)