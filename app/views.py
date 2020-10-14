from app import *
from app.controllers import *

@server.route("/")
def index():
	return render_template('index.html')