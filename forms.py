from flask_wtf import FlaskForm
from wtforms import StringField, FloatField


class AddCupcake(FlaskForm):
    """Form for adding cupcake"""

    flavor = StringField("Flavor")
    size = StringField("Size")
    rating = FloatField("Rating")
    image = StringField("Image")