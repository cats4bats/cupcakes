from app import db


class Cupcake(db.Model):
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String(15), nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False, default="https://tinyurl.com/demo-cupcake")
