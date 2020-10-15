from flask import Flask, redirect, request, render_template, jsonify 
# session
from models import db, connect_db, Cupcake
# import requests
from forms import AddCupcake

app = Flask(__name__)
app.config['SECRET_KEY'] = '46fyt' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/', methods=["GET", "POST"])
def index():
    """Shows cupcakes and form to add cupcakes - redirect after making new"""

    form = AddCupcake()

    if form.validate_on_submit():

        flavor = form.flavor.data
        size = form.size.data
        rating = form.rating.data
        image = form.image.data

        if image == '':
            c = Cupcake(flavor=flavor,size=size,rating=rating)
            db.session.add(c)
            db.session.commit()
        else:
            c = Cupcake(flavor=flavor,size=size,rating=rating,image=image)
            db.session.add(c)
            db.session.commit()

        return redirect('/')
        
    else:
        return render_template('/index.html', form=form)


@app.route('/api/cupcakes')
def cupcakes():
    """Gets data about all cupcakes"""

    cupcakes = Cupcake.query.all()
    todict = [Cupcake.to_dict(cupcake) for cupcake in cupcakes]

    return jsonify(cupcakes=todict)


@app.route('/api/cupcakes', methods=["POST"])
def create_new_cupcake():
    """Creates new cupcake"""

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']

    if image == '':
        c = Cupcake(flavor=flavor,size=size,rating=rating)
        db.session.add(c)
        db.session.commit()
    else:
        c = Cupcake(flavor=flavor,size=size,rating=rating,image=image)
        db.session.add(c)
        db.session.commit()

    todict = Cupcake.to_dict()

    return (jsonify(cupcake=todict), 201)


@app.route('/api/cupcakes/<int:cupcake_id>')
def cupcake(cupcake_id):
    """Gets data about specific cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    todict = Cupcake.to_dict(cupcake)

    return jsonify(cupcake=todict)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Updates data for specific cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    cupcake.flavor = request.json['flavor']
    cupcake.rating = request.json['rating']
    cupcake.size = request.json['size']
    cupcake.image = request.json['image']

    db.session.add(cupcake)
    db.session.commit()

    todict = Cupcake.to_dict()
    return jsonify(cupcake=todict)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Deletes specific cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")
