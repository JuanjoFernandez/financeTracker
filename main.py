from flask import Flask, render_template
from flask.views import MethodView

app = Flask(__name__)

class HomePage(MethodView):
    
    def get(self):
        return render_template("index.html")

class NewOperation(MethodView):

    def get(self):
        return render_template("new.html")

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/new', view_func=NewOperation.as_view('new'))

if __name__ == "__main__":
    app.run(debug = True)
