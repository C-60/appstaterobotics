from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/history/')
def history():
    return render_template ('history.html')

@app.route('/history/future')
def future():
	return render_template ('future.html')

@app.route('/history/urc')
def urc ():
	return render_template ('urc.html')

@app.route('/history/club')
def club ():
	return render_template('club.html')
	
@app.route('/aboutus')
def aboutus ():
    return render_template ('aboutus.html')

@app.route('/roaster')
def roaster ():
    return render_template ('roaster.html')

@app.route('/donate')
def donate ():
    return render_template ('donate.html')

@app.route('/socialmedia')
def socialmedia ():
    return render_template ('socialmedia.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return '%s' % username

if __name__ == "__main__":
    app.run()

