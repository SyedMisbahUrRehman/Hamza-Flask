from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/values', methods=['POST'])
def values():
    val1 = request.form['val1']
    val2 = request.form['val2']
    return redirect(url_for('display_values', val1=val1, val2=val2))

@app.route('/display_values/<val1>/<val2>')
def display_values(val1, val2):
    print("Your passed values are : ", val1, val2)
    return render_template('pass.html', val1=val1, val2=val2), 200


if __name__ == '__main__':
    app.run(debug=True)
