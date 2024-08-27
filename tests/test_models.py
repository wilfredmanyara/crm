#!/usr/bin/python3

import unittest
from app import create_app, db
from config import TestingConfig
from app.models import Farmer, Retailer, Product, Order, Transaction

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test variables and create app context."""
        self.app = create_app('testing')  # Use the testing configuration
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()  # Create all tables

    def tearDown(self):
        """Teardown app context and drop all tables."""
        db.session.remove()
        db.drop_all()  # Drop all tables
        self.app_context.pop()

    def add_farmer(self, name, email, phone_number, location):
        """Helper method to add a farmer."""
        farmer = Farmer(name=name, email=email, phone_number=phone_number, location=location)
        db.session.add(farmer)
        db.session.commit()
        return farmer

    def add_retailer(self, name, email, phone_number, location):
        """Helper method to add a retailer."""
        retailer = Retailer(name=name, email=email, phone_number=phone_number, location=location)
        db.session.add(retailer)
        db.session.commit()
        return retailer

    def add_product(self, name, description, price, quantity, farmer_id):
        """Helper method to add a product."""
        product = Product(name=name, description=description, price=price, quantity=quantity, farmer_id=farmer_id)
        db.session.add(product)
        db.session.commit()
        return product

    def add_order(self, quantity, total_price, retailer_id, product_id):
        """Helper method to add an order."""
        order = Order(quantity=quantity, total_price=total_price, retailer_id=retailer_id, product_id=product_id)
        db.session.add(order)
        db.session.commit()
        return order

    def add_transaction(self, amount, payment_method, order_id):
        """Helper method to add a transaction."""
        transaction = Transaction(amount=amount, payment_method=payment_method, order_id=order_id)
        db.session.add(transaction)
        db.session.commit()
        return transaction

    def test_farmer_creation(self):
        """Test creation of a Farmer."""
        farmer = self.add_farmer('John Doe', 'john@example.com', '1234567890', 'Farmville')
        self.assertIsNotNone(farmer.id, "Farmer ID should be assigned.")
        self.assertEqual(farmer.name, 'John Doe', "Farmer name should match.")

    def test_retailer_creation(self):
        """Test creation of a Retailer."""
        retailer = self.add_retailer('Jane Smith', 'jane@example.com', '0987654321', 'Retail Town')
        self.assertIsNotNone(retailer.id, "Retailer ID should be assigned.")
        self.assertEqual(retailer.email, 'jane@example.com', "Retailer email should match.")

    def test_product_creation(self):
        """Test creation of a Product."""
        farmer = self.add_farmer('Alice Johnson', 'alice@example.com', '5555555555', 'Green Acres')
        product = self.add_product('Tomatoes', 'Fresh organic tomatoes', 2.5, 100, farmer.id)
        self.assertIsNotNone(product.id, "Product ID should be assigned.")
        self.assertEqual(product.name, 'Tomatoes', "Product name should match.")
        self.assertEqual(product.farmer.name, 'Alice Johnson', "Product's farmer should match.")

    def test_order_creation(self):
        """Test creation of an Order."""
        retailer = self.add_retailer('Bob Brown', 'bob@example.com', '6666666666', 'City Market')
        farmer = self.add_farmer('Charlie Davis', 'charlie@example.com', '7777777777', 'Sunny Farm')
        product = self.add_product('Lettuce', 'Crisp green lettuce', 1.0, 50, farmer.id)
        order = self.add_order(20, 20.0, retailer.id, product.id)
        self.assertIsNotNone(order.id, "Order ID should be assigned.")
        self.assertEqual(order.product.name, 'Lettuce', "Order's product should match.")

    def test_transaction_creation(self):
        """Test creation of a Transaction."""
        retailer = self.add_retailer('Emily Clark', 'emily@example.com', '8888888888', 'Downtown Market')
        farmer = self.add_farmer('Frank Miller', 'frank@example.com', '9999999999', 'Harvest Fields')
        product = self.add_product('Carrots', 'Sweet orange carrots', 0.5, 200, farmer.id)
        order = self.add_order(100, 50.0, retailer.id, product.id)
        transaction = self.add_transaction(50.0, 'Credit Card', order.id)
        self.assertIsNotNone(transaction.id, "Transaction ID should be assigned.")
        self.assertEqual(transaction.order.retailer.name, 'Emily Clark', "Transaction's order retailer should match.")

if __name__ == '__main__':
    unittest.main()

