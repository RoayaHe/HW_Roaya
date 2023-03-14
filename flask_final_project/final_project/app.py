from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import os
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg', 'gif']
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
db = SQLAlchemy(app)
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
    director = db.Column(db.String(20), unique=False, nullable=False)
    release_year = db.Column(db.Integer, unique=False, nullable=False)
    filename = db.Column(db.String(100), unique=False, nullable=True)
    main_actors = db.Column(db.String, unique=False)
    budget = db.Column(db.String, unique=False)
    genre = db.Column(db.String, unique=False)
    duration = db.Column(db.String, unique=False)
    proper_age = db.Column(db.String, unique=False)
    video_link = db.Column(db.String, unique=False)
    def __repr__(self):
        return f"Title: {self.movie_title}, Director: {self.director}"
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    review_text = db.Column(db.String, unique=False, nullable=False)
    rate = db.Column(db.Integer, unique=False, nullable=False)
    def __repr__(self):
        return f"Name: {self.name}, Content:{self.review_text}, Rate:{self.rate}"
migrate = Migrate(app, db)
@app.route("/")
def home():
    movies_data = Movies.query.all()
    return render_template("index.html", movies_data=movies_data)

@app.route("/add_data")
def add_data():
    return render_template("add_profile.html")

@app.route("/add", methods=["POST", "GET"])
def movie_management():
    if request.method == "POST":
        movie_title = request.form.get("movie_title")
        description = request.form.get("description")
        director = request.form.get("director")
        release_year = request.form.get("release_year")
        file = request.files.get("filename")
        main_actors = request.form.get("main_actors")
        budget = request.form.get("budget")
        genre = request.form.get("genre")
        duration = request.form.get("duration")
        proper_age = request.form.get("proper_age")
        video_link = request.files.get("video")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        movie_row = Movies(movie_title=movie_title, description=description, director=director,
                           release_year=release_year, filename=file_name, main_actors=main_actors, budget=budget,
                           genre=genre, duration=duration, proper_age=proper_age, video_link=video_link)
        db.session.add(movie_row)
        db.session.commit()
        return redirect("/")

@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for('static', filename='uploads/'+filename))

@app.route("/movie_info/<movie_id>")
def movie_info(movie_id):
    movie_specific = Movies.query.get(movie_id)
    reviews_specific = Reviews.query.filter(Reviews.movie_id == movie_id)
    rate_specific = Reviews.query.filter(Reviews.movie_id == movie_id)
    return render_template("movie_info.html", movie_specific=movie_specific, reviews_specific=reviews_specific, rate_specific=rate_specific)

@app.route("/add_review", methods=["POST", "GET"])
def review_management():
    if request.method == "POST":
        name = request.form.get("name")
        review_text = request.form.get("review_text")
        rate = request.form.get("rate")
        movie_id = request.form.get("movie_id")
        review_row = Reviews(name=name, review_text=review_text, rate=rate, movie_id=movie_id,)
        db.session.add(review_row)
        db.session.commit()
        return redirect(url_for('movie_info', movie_id=movie_id))

@app.route("/delete/<int:id>")
def erase(id):
    data = Movies.query.get(id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}/{filename}")
    db.session.delete(data)
    reviews_specific = Reviews.query.filter(Reviews.movie_id == id)
    for review in reviews_specific:
        db.session.delete(review)
    db.session.commit()
    return redirect("/")

@app.route("/alter_movie/<int:id>", methods=["POST", "GET"])
def alter_movie(id):
    if request.method == "POST":
        data = Movies.query.get(id)
        movie_title = request.form.get("movie_title")
        description = request.form.get("description")
        director = request.form.get("director")
        release_year = request.form.get("release_year")
        file = request.files.get("filename")
        main_actors = request.form.get("main_actors")
        budget = request.form.get("budget")
        genre = request.form.get("genre")
        duration = request.form.get("duration")
        proper_age = request.form.get("proper_age")
        video_link = request.form.get("video_link")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        if request.form.get("movie_title"):
            data.movie_title = movie_title
        if request.form.get("description"):
            data.description = description
        if request.form.get("director"):
            data.director = director
        if request.form.get("release_year"):
            data.release_year = release_year
        if request.files.get("filename"):
            data.filename = file_name
        if request.form.get("main_actors"):
            data.main_actors = main_actors
        if request.form.get("budget"):
            data.budget = budget
        if request.form.get("genre"):
            data.genre = genre
        if request.form.get("duration"):
            data.duration = duration
        if request.form.get("proper_age"):
            data.proper_age = proper_age
        if request.form.get("video_link"):
            data.video_link = video_link
        db.session.commit()
        return redirect(url_for('movie_info', movie_id=id))
    else:
        return render_template("alter_movie.html")

class Watchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)

@app.route('/watchlist/<int:id>')
def add_to_watchlist(id):
    movies = Watchlist.query.all()
    _watchlist = Watchlist(movie_id=id)
    db.session.add(_watchlist)
    db.session.commit()
    return redirect(url_for('movie_info', movie_id=id))

@app.route('/watchlist_view')
def display_watchlist():
    movie_id = []
    movies = Watchlist.query.all()
    for movie in movies:
        movie_id.append(movie.movie_id)
    movie_id = list(set(movie_id))
    movie_watchlist = []
    for id in movie_id:
        movie_watchlist.append(Movies.query.get(id))
    return render_template('watchlist.html', movie_watchlist=movie_watchlist)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_value = request.form['search_string']
        search = "%{0}%".format(search_value)
        movies_data = Movies.query.filter(Movies.movie_title.like(search)).all()
        return render_template('index.html', movies_data=movies_data, pageTitle='Movies', legend="Search Results")
    else:
        return redirect("/")
if __name__ == "__main__":
    app.run()