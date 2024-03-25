from flask import Flask
from flask import render_template
from data import db_session
from data.users import User
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private is not True)
    return render_template("index.html", news=news)


if __name__ == '__main__':
    main()
