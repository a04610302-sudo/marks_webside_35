from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/',methods =['GET','POST'])
def home():
    if request.method == 'POST':
        markn = request.form.get('mark')
    else:
        markn = None

    return render_template('index.html',marks=markn)
app.run(debug=True)


