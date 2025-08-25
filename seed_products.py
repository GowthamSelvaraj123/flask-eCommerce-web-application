from app import create_app, db
from app.models import Product

app = create_app()

with app.app_context():
    Product.query.delete()  # Clear previous data

    sample_products = [
        {"name": "Laptop", "description": "High performance laptop", "price": 1200, "image_url":"/static/images/no_image_available.jpg", "stock": 10},
        {"name": "Smartphone", "description": "Latest Android phone", "price": 800, "image_url":"/static/images/no_image_available.jpg", "stock": 15},
        {"name": "Headphones", "description": "Noise cancelling headphones", "price": 200, "image_url":"/static/images/no_image_available.jpg", "stock": 20},
        {"name": "Smartwatch", "description": "Fitness smartwatch", "price": 150, "image_url":"/static/images/no_image_available.jpg", "stock": 12},
        {"name": "Camera", "description": "Digital SLR camera", "price": 500, "image_url":"/static/images/no_image_available.jpg", "stock": 8},
        {"name": "Backpack", "description": "Waterproof backpack", "price": 70, "image_url":"/static/images/no_image_available.jpg", "stock": 25},
        {"name": "Shoes", "description": "Running shoes", "price": 90, "image_url":"/static/images/no_image_available.jpg", "stock": 18},
        {"name": "Gaming Console", "description": "Next-gen console", "price": 400, "image_url":"/static/images/no_image_available.jpg", "stock": 5},
        {"name": "Desk Lamp", "description": "LED desk lamp", "price": 30, "image_url":"/static/images/no_image_available.jpg", "stock": 30},
        {"name": "Coffee Maker", "description": "Automatic coffee maker", "price": 120, "image_url":"/static/images/no_image_available.jpg", "stock": 7},
    ]

    for item in sample_products:
        db.session.add(Product(
            name=item["name"],
            description=item["description"],
            price=item["price"],
            image_url=item["image_url"],
            stock=item["stock"]
        ))

    db.session.commit()
    print("Sample products with images and stock added successfully!")
