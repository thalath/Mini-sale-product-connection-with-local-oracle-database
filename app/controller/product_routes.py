from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
from flask_login import login_required
from app.forms.product_forms import ProductCreaateForm, ProductEditeForm, ProductConFirmDeleteForm
from app.services.product_service import ProductService
product_bp = Blueprint("products", __name__, url_prefix="/products")

@product_bp.route("/")
@login_required
def index():
    products = ProductService.get_all()
    return render_template("products/index.html", products=products)


@product_bp.route("/<int:product_id>")
@login_required
def detail(product_id: int):
    product = ProductService.get_by_id(product_id)
    if product is None:
        abort(404)
    return render_template("products/detail.html", product=product)

@product_bp.route("/create", methods=["GET", "POST"])
def create():
    form = ProductCreaateForm()
    if form.validate_on_submit():
        data= {
            "product_no": form.product_no.data,
            "productname": form.productname.data,
            "profit_percent": form.profit_percent.data,
            "unit_meansure": form.unit_meansure.data,
            "reorder_level": form.reorder_level.data,
            "sell_price": form.sell_price.data,
            "cost_price": form.cost_price.data or 0.00,
            "qty_on_hand": form.qty_on_hand.data or 0, 
            "photo": form.photo.data or "No image found"
        }
        
        producttype = form.product_type.data or None
        
        product = ProductService.create(data, producttype)
        flash(f"Product: {product.productname} added successfully", "success")
        return redirect(url_for("products.index"))
    
    return render_template("products/create.html", form=form)

@product_bp.route("/<int:product_id>/edit", methods=["GET", "POST"])
def edit(product_id: int):
    product = ProductService.get_by_id(product_id)

    if product is None:
        abort(404)
        
    form = ProductEditeForm(original_product=product, obj=product)
    if form.validate_on_submit():
        data= {
            "product_no": form.product_no.data,
            "productname": form.productname.data,
            "profit_percent": form.profit_percent.data,
            "unit_meansure": form.unit_meansure.data,
            "reorder_level": form.reorder_level.data,
            "sell_price": form.sell_price.data,
            "cost_price": form.cost_price.data or 0.00,
            "qty_on_hand": form.qty_on_hand.data,
            "photo": form.photo.data
        }
        
        producttype = form.product_type.data or None
        
        ProductService.update(product, data, producttype)
        flash(f"Product '{product.productname}' updated successfully", "success")
        return redirect(url_for("products.index"))
    
    return render_template("products/edit.html", form=form, product=product.product_no)

@product_bp.route("/<int:product_id>/delete", methods=["GET"]) #methods get: just called data from database and asked for delete
@login_required
def delete_confirm(product_id: int):
    product = ProductService.get_by_id(product_id)
    if product is None:
        abort(404)

    form = ProductConFirmDeleteForm()
    return render_template("products/delete_confirm.html", product=product, form=form)


@product_bp.route("/<int:product_id>/delete", methods=["POST"]) # methods post: confirm deleted data from database 
@login_required
def delete(product_id: int):
    product = ProductService.get_by_id(product_id)
    if product is None:
        abort(404)

    ProductService.delete(product)
    flash("Products was deleted successfully.", "success")
    return redirect(url_for("Products.index"))