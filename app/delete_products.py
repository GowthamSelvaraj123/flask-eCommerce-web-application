from app import create_app, db
from app.models import Product

app = create_app()

with app.app_context():
    Product.query.delete()  # Deletes all products
    db.session.commit()
    print("All products deleted successfully!")