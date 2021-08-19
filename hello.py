from flask import Flask, redirect, url_for, render_template, request
from random import randrange
app = Flask(__name__)

mathTags = ["Algebra", "Coordinate Geometry", "Counting", "Data Interpretation", "Fraction", "Geometry", "Integer Properties", "Percents and Ratios", "Probability", "Statistics"]
AlgebraQuestions = []
CoGeoQuest	= []
CntQuest = []
DataInterQuest = []
FrctQuest = []
GeoQuest = []
IntPropQuest = []
PerRatQuest = []
ProbQuest = []
StatsQuest = []

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

# init the arrays with false based on the question count
def initializeLists():
	source = "static/Math/"
	# for each tag list do this
	for name in os.listdir(source):
		if os.path.isdir(os.path.join(a_dir, name)):
			source += name
			source += "/Question"
			mainDirNames = get_immediate_subdirectories(source)
			dirSize = len(mainDirNames)
			print name
			if "Algebra" in name:
				for n in range(dirSize):
					AlgebraQuestions.append(false)
					break
			if "Coordinate Geometry" in name:
				for n in range(dirSize):
					CoGeoQuest.append(false)
					break
			if "Counting" in name:
				for n in range(dirSize):
					CntQuest.append(false)
					break
			if "Data Interpretation" in name:
				for n in range(dirSize):
					DataInterQuest.append(false)
					break
			if "Fraction" in name:
				for n in range(dirSize):
					FrctQuest.append(false)
					break
			if "Geometry" in name:
				for n in range(dirSize):
					GeoQuest.append(false)
					break
			if "Integer Properties" in name:
				for n in range(dirSize):
					IntPropQuest.append(false)
					break
			if "Percents and Ratios" in name:
				for n in range(dirSize):
					PerRatQuest.append(false)
					break
			if "Probability" in name:
				for n in range(dirSize):
					ProbQuest.append(false)
					break
			if "Statistics" in name:
				for n in range(dirSize):
					StatsQuest.append(false)
					break

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

def GetQuestion(tag):
	if "Math" in tag:
		val = randrange(len(mathTags))
		return GetQuestion(mathTags[val])
	if "Algebra" in name:
	for n in range(dirSize):
		AlgebraQuestions.append(false)
		break
	if "Coordinate Geometry" in name:
	for n in range(dirSize):
		CoGeoQuest.append(false)
		break
	if "Counting" in name:
	for n in range(dirSize):
		CntQuest.append(false)
		break
	if "Data Interpretation" in name:
	for n in range(dirSize):
		DataInterQuest.append(false)
		break
	if "Fraction" in name:
	for n in range(dirSize):
		FrctQuest.append(false)
		break
	if "Geometry" in name:
	for n in range(dirSize):
		GeoQuest.append(false)
		break
	if "Integer Properties" in name:
	for n in range(dirSize):
		IntPropQuest.append(false)
		break
	if "Percents and Ratios" in name:
	for n in range(dirSize):
		PerRatQuest.append(false)
		break
	if "Probability" in name:
	for n in range(dirSize):
		ProbQuest.append(false)
		break
	if "Statistics" in name:
	for n in range(dirSize):
		StatsQuest.append(false)
		break
		#randomly choose based on the selected tag

	return imgUrl

@app.route('/result', methods=['POST','GET'])
def result():
	if request.method == 'POST':
		question = request.form['reply']
		if question == "Question":
			imgUrl = GetQuestion(tag)
			#imgUrl ='static/Math/Algebra/Question/1/Capture.jpg'
			#Url = url_for('static', filename={{imgUrl}})
			return render_template("question.html", Value=imgUrl)
		if question == "Video":
			return render_template("video.html")
		if question == "Answer":
			return render_template("image.html")

@app.route('/PrepTool')
def prep_tool():
	initializeLists()
	return render_template('index.html')

@app.route('/')
def landing_page():
	return render_template('GrayScale.html')

if __name__ == '__main__':
	app.add_url_rule('/home',view_func=home_page)
	app.run(debug=True)
