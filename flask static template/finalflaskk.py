from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='homepage',status='')

@app.route('/about')
def about():
    return render_template('about.html',title='about',status='')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html',title='Predictor',status='')

@app.route('/forest_fire')
def forest_fire():
    return render_template('forest_fire.html',title='forest_fire',status='')



@app.route('/services')
def services():
    return render_template('services.html',title='services',status='')

if __name__ =='__main__':
    app.run(debug=True)