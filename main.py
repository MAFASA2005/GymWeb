from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def Home():
    return render_template('index2.html')

@app.route('/services')
def Services():
    return render_template('Services.html')

@app.route('/about us')
def About_Us():
    return render_template('About US.html')

@app.route('/pricing')
def Pricing():
    return render_template('Pricing.html')

@app.route('/review')
def Review():
    return render_template('Review.html')

if __name__ == '__main__' :
    app.run(debug=True)