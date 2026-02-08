from extensions import db
from typing import List, Optional
from app.models.products import Product
from werkzeug.datastructures import FileStorage
from app.models.product_types import Product_type


class ProductService:
    
    @staticmethod
    def get_all() -> List[Product]:
        return Product.query.order_by(Product.product_no.asc()).all()
    
    @staticmethod
    def get_by_id(product_id: int) -> Optional[Product]:
        return Product.query.get(product_id)

    @staticmethod
    def create(data: dict, producttype: Optional[int] = None) -> Product:
        product = Product(
            product_no = data["product_no"],
            productname = data["productname"],
            profit_percent = data["[profit_percent]"],
            unit_meansure = data["unit_meansure"],
            reorder_level = data["reorder_level"],
            sell_price = data["sell_price"] or 0,
            cost_price = data["cost_price"] or 0,
            qty_on_hand = data.get("qty_on_hand", default=0),
            photo = data.get("photo") or "image not found"
        )
        
        if producttype:
            pt = db.session.get(Product_type, producttype)
            if pt:
                product.producttype = [pt]

        db.session.add(product)    
        db.session.commit()
        return product
    
    @staticmethod
    def update(product: Product, data: dict, producttype: Optional[int] = None) -> Product:
        product.product_no = data["product_no"]
        product.productname = data["productname"]
        product.profit_percent = data["profit_percent"]
        product.unit_meansure = data["unit_meansure"]
        product.reorder_level = data["reorder_level"]
        product.sell_price = data["sell_price"]
        product.cost_price = data["cost_price"]
        product.qty_on_hand = data["qty_on_hand"]
        
        if producttype:
            pt = db.session.get(Product_type, producttype)
            if pt:
                product.producttype = [pt]
            
        db.session.commit()
        return product
    
    @staticmethod
    def delete(product: Product):
        db.session.delete(product)
        db.session.commit()
