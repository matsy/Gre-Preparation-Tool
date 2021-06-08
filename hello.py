from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

def home_page():
	return "<p> This is being used to test the decorator 'add_url_rule' </p>"

@app.route('/admin')
def hello_admin():
	return "<p>Hello Admin</p>"

@app.route('/guest/<guest>')
def hello_guest(guest):
	return "<p>Hello %s as Guest</p>" % guest

@app.route('/user/<name>')
def hello_user(name):
	if name =='admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest', guest=name))

@app.route('/hello/')
def hello_name():
	return render_template('hello.html')

@app.route('/result', methods=['POST','GET'])
def result():
	if request.method == 'POST':
		question = request.form['reply']
		if question == "Question":
			return render_template("question.html", question=question)
		if question == "Video":
			return render_template("video.html")
		if question == "Answer":
			return render_template("image.html")
			
@app.route('/PrepTool')
def prep_tool():
	return render_template('index.html')

@app.route('/')
def landing_page():
	return render_template('GrayScale.html')

if __name__ == '__main__':
	app.add_url_rule('/home',view_func=home_page)
	app.run(debug=True)