from flask import Flask, render_template, request 
import joblib

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/prediccion',methods=['POST'])
def prediccion():
    importe_total = float(request.form['importe_total'])
    numero_personas = float(request.form['numero_personas'])
    modelo = joblib.load('app/modelo/propinas.pkl')
    prediccion = modelo.predict([[importe_total, numero_personas]])
    return render_template('index.html', prediccion=f"La prediccion de propinas es {prediccion[0]:.2f}€")
if __name__=='__main__':
    app.run(debug=True)