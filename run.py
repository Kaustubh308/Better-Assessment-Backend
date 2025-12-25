from flask import Flask
from app.extensions import db
from app.routes.comments import comments_bp


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(comments_bp)

    with app.app_context():
        db.create_all()   # ✅ creates tables safely

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
