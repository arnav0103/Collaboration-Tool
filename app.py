from Tool import app, db
from Tool.models import User,Team,Upcoming,Ongoing,Completed
from flask import render_template,request, url_for
from flask_login import current_user

@app.route('/')
def index():
    return render_template("index.htm")

if __name__ == '__main__':
    app.run(debug=True)
