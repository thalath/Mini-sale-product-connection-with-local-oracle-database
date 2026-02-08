from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length
from extensions import db
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.models.product_types import Product_type
from app.models.products import Product

def _type_choices():
    return [
        (p.producttype_id, p.producttype_name)
        for p in db.session.scalars(
            db.select(Product_type).order_by(Product_type.producttype_id)
        )
    ]

class ProductCreaateForm(FlaskForm):
    product_no = StringField(
        "Product ID",
        validators=[DataRequired()],
        render_kw={"placeholder": "e.g. P001"}
    )
    
    productname = StringField(
        "Product Name",
        validators=[DataRequired(), Length(min=2, max=39)],
        render_kw={"placeholder": "Enter Product Name"}
    )
    
    product_type = SelectField(
        "Select type",
        coerce=int,
        validate_choice=[DataRequired()]
    )
    
    profit_percent = IntegerField(
        "Enter Profit_percent",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter profit Percent"}
    )
    
    unit_meansure = StringField(
        "Unit_meansure",
        validators=[DataRequired(), Length(min=3, max=14)],
        render_kw={"placeholder": "Enter Unit meansure"}
    )
    
    reorder_level = IntegerField(
        "Reorder_level",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level"}
    )
    
    sell_price = FloatField(
        "Sell price",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter sell price"}
    )
    
    cost_price = FloatField(
        "cost price",
        validators=[DataRequired()],
        render_kw={"placeholder": "enter cost price"}
    )
    
    qty_on_hand = IntegerField(
        "Qty in Stock",
        render_kw={"placeholder": "Enter Qty in stock"}
    )
    
    photo = FileField(
        "Binary file (PDF or Image)",
        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'pdf'], 'Files only!')],
    )
    
    submit = SubmitField("Save")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_type.choices = _type_choices()


class ProductEditeForm(FlaskForm):
    product_no = StringField(
        "Product ID",
        validators=[DataRequired()],
        render_kw={"placeholder": "e.g. P001"}
    )
    
    productname = StringField(
        "Product Name",
        validators=[DataRequired(), Length(min=2, max=39)],
        render_kw={"placeholder": "Enter Product Name"}
    )
    
    product_type = SelectField(
        "Select type",
        coerce=int,
        validate_choice=[DataRequired()]
    )
    
    profit_percent = IntegerField(
        "Enter Profit_percent",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter profit Percent"}
    )
    
    unit_meansure = StringField(
        "Unit_meansure",
        validators=[DataRequired(), Length(min=3, max=14)],
        render_kw={"placeholder": "Enter Unit meansure"}
    )
    
    reorder_level = IntegerField(
        "Reorder_level",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level"}
    )
    
    sell_price = FloatField(
        "Sell price",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter sell price"}
    )
    
    cost_price = FloatField(
        "cost price",
        validators=[DataRequired()],
        render_kw={"placeholder": "enter cost price"}
    )
    
    qty_on_hand = IntegerField(
        "Qty in Stock",
        render_kw={"placeholder": "Enter Qty in stock"}
    )
    
    photo = FileField(
        "Binary file (PDF or Image)",
        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'pdf'], 'Files only!')],
    )
    
    submit = SubmitField("Update")

    def __init__(self, original_product: Product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_product = original_product
        self.product_type.choices = _type_choices()
        
class ProductConFirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")
    