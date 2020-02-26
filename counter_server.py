from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' in session:
        print('count exists!')
    else:
        session['count'] = 0
    if 'user' in session:
        print('user exists!')
        session['user'] += 1
    else:
        session['user'] = 0
    return render_template("counter_index.html")

@app.route('/increase', methods=['POST'])
def increase():
    session['count'] += 1
    return redirect('/')

@app.route('/increase_two', methods=['POST'])
def increase_two():
    session['count'] += 2
    return redirect('/')

@app.route('/increase_number', methods=['POST'])
def increase_number():
    number = int(request.form['number'])
    session['count'] += number
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    session['user'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)