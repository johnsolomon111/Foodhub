from app import *
from app.controllers import *

@server.route("/", methods=["GET"])
def index():
	return render_template('index.html')

@server.route("/signup", methods=["GET", "POST"])
def signup():
	messege = ""
	form_dict = {
		"first_name" : "",
		"last_name" : "",
		"email" : ""
	}
	if request.method == "POST":
		if request.form["confirm_password"] == request.form["password"]:
			print(request.form["password"])
			return redirect(url_for('home'))
		else:
			form_dict["first_name"] = request.form["first_name"]
			form_dict["last_name"] = request.form["last_name"]
			form_dict["email"] = request.form["email"]

			messege = "Password does not match"
			print(messege)
			return render_template("auth/signup.html", messege=messege, form_dict= form_dict)
	return render_template("auth/signup.html", messege=messege, form_dict= form_dict)

@server.route("/home", methods=["GET", "POST"])
def home():
	return "Hiiii!!!!!"