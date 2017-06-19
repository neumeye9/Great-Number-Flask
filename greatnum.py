import random
from flask import Flask, render_template, redirect, session, request
app=Flask(__name__)
app.secret_key='kristakrista'
num = random.randint(1,101)


@app.route('/')
def index():
    print num
    return render_template('index.html', result=session['result'])

@app.route('/guess', methods=['POST'])
def guess():

    session['text'] = request.form['text']
    guess = session['text']
    print guess

    if int(guess) == num: 
        print "hi"
        session['result']= "You guessed the right number, it is" + " " + str(num)

    elif int(guess) < num:
        print "bye"
        session['result'] = "Too low, try again"

    elif int(guess) > num:
        print "nope"
        session['result'] = "Too high, try again"

    return redirect('/')




app.run(debug=True)