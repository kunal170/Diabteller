from flask import Flask,render_template,request
from data_cleaning import data_cleaning
from data_training import data_training
app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def home():
    
    if(request.method == "POST"):
        return render_template("result.html")
    return render_template("index.html")


@app.route('/result',methods=['GET','POST'])
def result():
    data_cleaning()
    
    if(request.method=="POST"):
        result = request.form
        #print(result)
        values= data_training(result)
        print(values[0])
        return render_template("result.html",values=values)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)