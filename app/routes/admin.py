from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.decorators import admin_required
from app.models import Product, User, Category, Order
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    products = Product.query.all()
    return render_template('admin/dashboard.html', products=products)

@admin_bp.route('/products')
@login_required
@admin_required
def manage_products():
    products = Product.query.all()
    return render_template('admin/products.html', products=products)

@admin_bp.route('/products/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_product():
    categories = Category.query.all()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        category_id = request.form.get('category_id') or None
        image_url = request.form.get('image_url')

        new_product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock,
            category_id=category_id,
            image_url=image_url
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin.manage_products'))

    return render_template('admin/add_product.html', categories=categories)

# Edit product
@admin_bp.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    categories = Category.query.all()
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = float(request.form['price'])
        product.stock = int(request.form['stock'])
        product.category_id = request.form.get('category_id') or None
        product.image_url = request.form.get('image_url')
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin.manage_products'))

    return render_template('admin/edit_product.html', product=product, categories=categories)

# Delete product
@admin_bp.route('/products/delete/<int:product_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully!', 'danger')
        return redirect(url_for('admin.manage_products'))

    return render_template('admin/delete_product.html', product=product)

@admin_bp.route('/users')
@login_required
@admin_required
def manage_users():
    products = Product.query.all()
    return render_template('admin/users.html')

@admin_bp.route('/orders')
@login_required
@admin_required
def manage_orders():
    products = Product.query.all()
    return render_template('admin/orders.html')

@admin_bp.route('/categories')
@login_required
@admin_required
def manage_categories():
    products = Product.query.all()
    return render_template('admin/categories.html')
