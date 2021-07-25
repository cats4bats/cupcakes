from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'

db = SQLAlchemy(app)

from models import Cupcake


@app.route('/api/cupcakes')
def cupcakes():
    cupcakes = [{'id':c.id, 'flavor':c.flavor, 'size':c.size, 'rating':c.rating, 'image':c.image} for c in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<id>')
def get_cupcake(id):
    c = Cupcake.query.get_or_404(id)
    return jsonify(cupcake={'id':c.id, 'flavor':c.flavor, 'size':c.size, 'rating':c.rating, 'image':c.image})

@app.route('/api/cupcakes', methods=['POST'])
def post_cupcake():
    f = request.json.get('flavor')
    r = request.json.get('rating')
    i = request.json.get('image')
    s = request.json.get('size')

    cupcake = Cupcake(flavor=f, rating=r, image=i, size=s)
    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake={'image':i, 'flavor':f, 'rating':r, 'size':s})

@app.route('/api/cupcakes/<id>', methods=['PATCH'])
def patch_cupcake(id):
    f = request.json.get('flavor')
    r = request.json.get('rating')
    i = request.json.get('image')
    s = request.json.get('size')

    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = f
    cupcake.rating = r
    cupcake.image = i
    cupcake.size = s

    db.session.commit()

    return jsonify(cupcake={'image':i, 'flavor':f, 'rating':r, 'size':s})

@app.route('/api/cupcakes/<id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")

@app.route('/')
def root():
    return render_template('index.html')
