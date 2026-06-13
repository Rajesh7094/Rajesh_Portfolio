from flask import Flask, render_template, redirect
import json

app = Flask(__name__)

def load_data():
    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.route('/')
def home():
    data = load_data()
    return render_template("index.html", data=data)

# Redirect old multi-page routes to single-page anchors
@app.route('/projects')
def projects():
    return redirect('/#projects')

@app.route('/contact')
def contact():
    return redirect('/#contact')

@app.route('/certificates')
def certificates():
    return redirect('/#certificates')

@app.route('/resume')
def resume():
    return redirect('/#resume')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)