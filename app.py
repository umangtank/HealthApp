from flask import Flask,render_template,request
from joblib import load

with open("Notebook\model.sav", "rb") as f:
    model = load(f)

app = Flask(__name__)

@app.route('/')
def HomePage():
    return render_template('home.html')

@app.route('/Diabetes')
def DiabetesPage():
    return render_template('diabetes.html')

@app.route('/predict_D',methods=['POST', 'GET'])
def CheckDiabetesPage():
    if request.method == 'POST':
        try:
            print(request.form)
            user_data = request.form.to_dict()
            # print(user_data)

            Pregnancies = int(request.form['pregnancies'])
            print(Pregnancies)
            Glucose = int(request.form['glucose'])
            print(Glucose)
            BloodPressure = int(request.form['bloodpressure'])
            print(BloodPressure)
            SkinThickness = int(request.form['skinthickness'])
            print(SkinThickness)
            Insulin = int(request.form['insulin'])
            BMI = float(request.form['bmi'])
            DiabetesPedigreeFunction = float(request.form['dpf'])
            Age = int(request.form['age'])
                    
            data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            # user_data = list(user_data.values())
            output = model.predict([data])

            if output == 1:
                output = "Diabetic"
            else:
                output = "Not Diabetic"
                
        except Exception as e:
            output = f"Error: {e}"
             
        return render_template('diabetes.html', user_data = output)

    else:
        return render_template('diabetes.html')
    

if __name__ == '__main__':
    app.run(debug=True)