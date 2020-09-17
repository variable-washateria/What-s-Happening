from app import app
from app.tasks import mohawkenvelope, parishshow
from app.tasks2 import numaddition, querysearch

from flask import render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField

placer2 = "Friends"


@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('greeting.html', say=request.form['say'], to=request.form['to'])


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/tasks")
def test():
	return mohawkshow

@app.route("/yourresults", methods=['GET', 'POST'])
def yourresults():
	if request.method == 'POST':
		#print(request.form.getlist("venue"))
		checked_venues = request.form.getlist("venue")
		date = request.form.get("date")
		return render_template("yourresults.html", checked_venues = checked_venues, theywantasee1 = mohawkenvelope, theywantasee2 = parishshow, theywantasee3 = placer2, date = date)
	else:
		return "hi"	


@app.route("/fuckbugs")
def fuckbugs():
	return render_template("fuckbugs.html")


#bug testing: taking out search item from (), <searchitem> here/ and passed along argument from url_for on  yourresults.html
@app.route("/listen1")
def listen1():
	#bandname = request.args.get("bandname")
	bandname = "This is " 
	task2a = numaddition(bandname)

	searchitem = "bleh bleh"
	task2b = querysearch(searchitem)

	return render_template('listen1.html', searchitem = searchitem, somelamenum = task2a, thirdprint = task2b)

    
@app.route("/youtubetest")
def youtubetest():
	return render_template("youtubetest.html")

@app.route("/youtubetest2", methods= ['POST','GET'] )
def youtubetest2():
	
	return ''' <form method = 'POST', 'GET' action = "https://www.youtube.com/results?search_query=name">
	<input type = "text" name = "band" >
	<input type = "submit"> </form>  '''



@app.route("/shows")
def shows():
	return render_template("shows.html")

