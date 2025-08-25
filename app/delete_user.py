from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    num_deleted = User.query.delete()  # Delete all users
    db.session.commit()
    print(f"Deleted {num_deleted} users from the database.")
