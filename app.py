from flask import Flask, render_template, url_for, request, redirect
from sqlalchemy import text
from models import db, User, Email

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)	

with app.app_context():
    db.create_all()
    
@app.route("/")
def index():
    user_from_db = db.session.query(User).all()
    return render_template("index.html", users=user_from_db)  

@app.route("/search_user", methods=["POST"])
def search_username():
    search_term = request.form.get('search')
    user_found = db.session.query(User).filter(User.username == search_term).all()
    return render_template('index.html', users=user_found)

@app.route("/user_form")
def user_form():
    return render_template("user_form.html")

@app.route("/user_edit/<int:user_id>")
def user_edit(user_id):
    user_data = User.query.get_or_404(user_id)
    return render_template("user_edit.html", user=user_data)

@app.route("/user_insert", methods=["POST"])
def user_insert():
    #print(request.form)
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    new_user = User(        
          username = request.form["username"]
        , password = request.form["password"]
    )
    new_email = Email(
          email = email
        , user  = new_user  #associate email with user
    )
    db.session.add(new_user)
    db.session.add(new_email)
    db.session.commit()
    return redirect( url_for('index') )

@app.route("/user_delete/<int:user_id>")
def user_delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)     #DB DELETE
    db.session.commit()
    return redirect( url_for('index'))


@app.route("/user_update/<int:user_id>", methods=["POST"])
def user_update(user_id):
    username = request.form.get('username')
    email    = request.form.get('email')
    password = request.form.get('password')
    user = User.query.get_or_404(user_id)
    user.username = username  
    user.email    = email
    user.password = password   #buids and UPDATE
    db.session.commit()

    return redirect( url_for('index') )

if __name__ == '__main__':
    app.run(debug=True, port=5000)