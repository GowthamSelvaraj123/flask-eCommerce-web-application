from flask import Blueprint, render_template, request, redirect, url_for
from app.models import User, Product
from app import db
from flask_login import login_user, logout_user, login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = User(
            username=request.form['username'],
            email=request.form['email'],
            password=request.form['password'],
            is_admin=True if 'is_admin' in request.form else False
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main_bp.route('/cart')
@login_required
def cart():
    cart_items = []  # implement cart logic later
    total = sum(item.product.price * item.quantity for item in cart_items) if cart_items else 0
    return render_template('cart.html', cart_items=cart_items, total=total)

@main_bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    return redirect(url_for('main.cart'))

@main_bp.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)
