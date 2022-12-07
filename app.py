from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def HomePage():
    return render_template('home.html')

@app.route('/Diabetes')
def DiabetesPage():
    return render_template('diabetes.html')

if __name__ == '__main__':
    app.run(debug=True)