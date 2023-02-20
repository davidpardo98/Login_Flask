from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/app_1.db'
db = SQLAlchemy(app)

class registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    email = db.Column(db.String(200))
    contra = db.Column(db.String(200))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/registro')
def registro():
    return render_template("registro.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/agregar', methods=['POST'])
def agregar():
    crear = registro(nombre=request.form['name'], email=request.form['email'], contra=request.form['password'])
    db.session.add(crear)
    db.session.commit()
    return 'save'
    
if __name__ == '__main__':
    app.run(debug=True)