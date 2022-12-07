from flask import Flask,render_template,request
import pickle


# Load the Decision Tree Classifier model
model = pickle.load(open('Notebook\model.pkl', 'rb'))

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
            user_data = request.form.to_dict()
            Pregnancies = int(user_data['Pregnancies'])
            Glucose = int(user_data['Glucose'])
            BloodPressure = int(user_data['BloodPressure'])
            SkinThickness = int(user_data['SkinThickness'])
            Insulin = int(user_data['Insulin'])
            BMI = float(user_data['BMI'])
            DiabetesPedigreeFunction = float(user_data['DiabetesPedigreeFunction'])
            Age = int(user_data['Age'])
            data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            # user_data = list(user_data.values())
            output = model.predict([data])
        except Exception as e:
            output = f"Error: {e}"
             
        return render_template('diabetes.html', user_data=output)

    else:
        return render_template('diabetes.html')
    

if __name__ == '__main__':
    app.run(debug=True)