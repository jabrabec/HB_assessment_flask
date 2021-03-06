from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import jinja2

app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show an application page with submittable form."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def process_application():
    """Process the input from the application form and confirm receipt."""

    # # alternate methods to retrieve POST input:
    # first_name = request.form["firstname"]
    # last_name = request.form["lastname"]
    # job = request.form["job"]
    # salary = request.form["salary"]
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    job = request.form.get("job")
    salary = request.form.get("salary")

    return render_template("application-response.html", firstname=first_name,
                           lastname=last_name, job=job, salary=salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
