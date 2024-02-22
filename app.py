from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pass.html', methods=['POST'])
def pass_data():
    if request.method == 'POST':
        bname1 = request.form.get('bname1')
        bname2 = request.form.get('bname2')
        print("Button 1:", bname1)
        print("Button 2:", bname2)
        return render_template('pass.html', bname1=bname1, bname2=bname2)
    else:
        return "Method Not Allowed", 405

if __name__ == '__main__':
    app.run(debug=True)
