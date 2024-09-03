#!/usr/bin/python3

import unittest
from app import create_app, db
from app.models import Farmer, Retailer, Product, Order, Transaction
from flask import json


class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_farmer(self):
        response = self.client.post('/farmers', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'location': 'Nairobi'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Farmer created', response.get_data(as_text=True))

    def test_get_farmers(self):
        with self.app.app_context():
            farmer = Farmer(name='John Doe', email='john@example.com', phone_number='1234567890', location='Nairobi')
            db.session.add(farmer)
            db.session.commit()

        response = self.client.get('/farmers')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', response.get_data(as_text=True))

    # Test cases for retailers
    def test_create_retailer(self):
        response = self.client.post('/retailers', json={
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone_number': '9876543210',
            'location': 'Mombasa'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Retailer created', response.get_data(as_text=True))

    def test_get_retailers(self):
        with self.app.app_context():
            retailer = Retailer(name='Jane Doe', email='jane@example.com', phone_number='9876543210', location='Mombasa')
            db.session.add(retailer)
            db.session.commit()

        response = self.client.get('/retailers')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Jane Doe', response.get_data(as_text=True))

    # Test cases for product
    def test_create_product(self):
        with self.app.app_context():
            farmer = Farmer(name='John Doe', email='john@example.com', phone_number='9876543210', location='Nairobi')
            db.session.add(farmer)
            db.session.commit()

            response = self.client.post('/products', json={
                'name': 'Tomatoes',
                'description': 'Fresh red tomatoes',
                'price': 50.0,
                'quantity': 100,
                'farmer_id': farmer.id
            })
            self.assertEqual(response.status_code, 201)
            self.assertIn('Product created', response.get_data(as_text=True))

    def test_get_products(self):
        with self.app.app_context():
            farmer = Farmer(name='John Doe', email='john@example.com', phone_number='1234567890', location='Nairobi')
            db.session.add(farmer)
            db.session.commit()

            product = Product(name='Tomatoes', description='Fresh red tomatoes', price=50.0, quantity=100, farmer_id=farmer.id)
            db.session.add(product)
            db.session.commit()

            response = self.client.get('/products')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Tomatoes', response.get_data(as_text=True))

    # Test cases for Order model
    def test_create_order(self):
        with self.app.app_context():
            retailer = Retailer(name='Jane Smith', email='jane@example.com', phone_number='0987654321', location='Mombasa')
            db.session.add(retailer)
            db.session.commit()
            farmer = Farmer(name='John Doe', email='john@example.com', phone_number='1234567890', location='Nairobi')
            db.session.add(farmer)
            db.session.commit()
            product = Product(name='Tomatoes', description='Fresh red tomatoes', price=50.0, quantity=100, farmer_id=farmer.id)
            db.session.add(product)
            db.session.commit()

            response = self.client.post('/orders', json={
                'quantity': 10,
                'total_price': 500.0,
                'retailer_id': retailer.id,
                'product_id': product.id
            })
            self.assertEqual(response.status_code, 201)
            self.assertIn('Order created', response.get_data(as_text=True))

    def test_get_orders(self):
        with self.app.app_context():
            retailer = Retailer(name='Jane Smith', email='jane@example.com', phone_number='0987654321', location='Mombasa')
            db.session.add(retailer)
            db.session.commit()
            farmer = Farmer(name='John Doe', email='john@example.com', phone_number='1234567890', location='Nairobi')
            db.session.add(farmer)
            db.session.commit()
            product = Product(name='Tomatoes', description='Fresh red tomatoes', price=50.0, quantity=100, farmer_id=farmer.id)
            db.session.add(product)
            db.session.commit()
            order = Order(quantity=10, total_price=500.0, retailer_id=retailer.id, product_id=product.id)
            db.session.add(order)
            db.session.commit()

            response = self.client.get('/orders')
            self.assertEqual(response.status_code, 200)
            self.assertIn('product_id', response.get_data(as_text=True))

    # Test cases for Transaction model
    def test_create_transaction(self):
        with self.app.app_context():
            retailer = Retailer(name='Jane Smith', email='jane@example.com', phone_number='0987654321', location='Mombasa')
            db.session.add(retailer)
            db.session.commit()
            farmer = Farmer(name='John Doe', email='john@example.com', phone_number='1234567890', location='Nairobi')
            db.session.add(farmer)
            db.session.commit()
            product = Product(name='Tomatoes', description='Fresh red tomatoes', price=50.0, quantity=100, farmer_id=farmer.id)
            db.session.add(product)
            db.session.commit()
            order = Order(quantity=10, total_price=500.0, retailer_id=retailer.id, product_id=product.id)
            db.session.add(order)
            db.session.commit()

            response = self.client.post('/transactions', json={
                'amount': 500.0,
                'payment_method': 'Mpesa',
                'order_id': order.id
            })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Transaction created', response.get_data(as_text=True))

    def test_get_transactions(self):
        with self.app.app_context():
            retailer = Retailer(name='Jane Smith', email='jane@example.com', phone_number='0987654321', location='Mombasa')
            db.session.add(retailer)
            db.session.commit()
            farmer = Farmer(name='John Doe', email='john@example.com', phone_number='1234567890', location='Nairobi')
            db.session.add(farmer)
            db.session.commit()
            product = Product(name='Tomatoes', description='Fresh red tomatoes', price=50.0, quantity=100, farmer_id=farmer.id)
            db.session.add(product)
            db.session.commit()
            order = Order(quantity=10, total_price=500.0, retailer_id=retailer.id, product_id=product.id)
            db.session.add(order)
            db.session.commit()
            transaction = Transaction(amount=500.0, payment_method='Mpesa', order_id=order.id)
            db.session.add(transaction)
            db.session.commit()

            response = self.client.get('/transactions')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Mpesa', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
