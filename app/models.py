#!/usr/bin/python3

from datetime import datetime, timezone
from app import db

class Farmer(db.Model):
    __tablename__ = 'farmers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    
    products = db.relationship('Product', backref='farmer', lazy=True)
    
    def __repr__(self):
        return f"<Farmer {self.name}>"

class Retailer(db.Model):
    __tablename__ = 'retailers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    
    orders = db.relationship('Order', backref='retailer', lazy=True)
    
    def __repr__(self):
        return f"<Retailer {self.name}>"

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))  # Updated to use timezone-aware UTC
    
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.id'), nullable=False)
    
    def __repr__(self):
        return f"<Product {self.name}>"

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    date_ordered = db.Column(db.DateTime, default=datetime.now(timezone.utc))  # Updated to use timezone-aware UTC
    
    retailer_id = db.Column(db.Integer, db.ForeignKey('retailers.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    
    product = db.relationship('Product')
    
    def __repr__(self):
        return f"<Order {self.id}>"

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    date_paid = db.Column(db.DateTime, default=datetime.now(timezone.utc))  # Updated to use timezone-aware UTC
    
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    
    order = db.relationship('Order')
    
    def __repr__(self):
        return f"<Transaction {self.id}>"

