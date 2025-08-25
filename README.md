<body>
    <h1>Flask eCommerce Web Application</h1>
    <p>This is a <strong>full-featured eCommerce web application</strong> built using <strong>Flask</strong>, <strong>SQLAlchemy</strong>, and <strong>Flask-Login</strong>. The project demonstrates a complete workflow for managing products, users, orders, and categories in an online store environment.</p>
    <h2>Features</h2>
    <ul>
        <li>User registration, login, and logout with session management</li>
        <li>Admin panel for managing products, users, orders, and categories</li>
        <li>Add, edit, and delete products with category assignment and stock management</li>
        <li>Product listing and detail pages for customers</li>
        <li>Cart functionality (add/remove products)</li>
        <li>Responsive front-end using Bootstrap</li>
        <li>Secure authentication and admin authorization</li>
    </ul>
    <h2>Tech Stack</h2>
    <ul>
        <li><strong>Backend:</strong> Python, Flask, Flask-Login, Flask-Migrate, SQLAlchemy</li>
        <li><strong>Database:</strong> SQLite (can be replaced with MySQL/PostgreSQL)</li>
        <li><strong>Frontend:</strong> HTML, CSS, Bootstrap, Jinja2 templating</li>
    </ul>
    <h2>Folder Structure</h2>
    <pre>
ecommerce-flask/
│
├── app/
│   ├── models.py
│   ├── __init__.py
│   ├── routes/
│   │   ├── main.py
│   │   └── admin.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       └── admin/
│           ├── dashboard.html
│           ├── products.html
│           ├── add_product.html
│           ├── edit_product.html
│           ├── delete_product.html
│           ├── users.html
│           ├── orders.html
│           └── categories.html
├── migrations/
├── seed_products.py
├── run.py
└── requirements.txt
    </pre>
    <h2>How to Run</h2>
    <ol>
        <li>Clone the repository:<br>
            <pre>git clone &lt;your-repo-url&gt;
cd ecommerce-flask</pre>
        </li>
        <li>Create a virtual environment and install dependencies:<br>
            <pre>python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt</pre>
        </li>
        <li>Run database migrations:<br>
            <pre>flask db upgrade</pre>
        </li>
        <li>Start the Flask server:<br>
            <pre>flask run</pre>
        </li>
        <li>Open the application at <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a></li>
    </ol>
    <h2>License</h2>
    <p>MIT License</p>
    <h2>Author</h2>
    <p>Gowtham S - Fullstack Developer</p>
</body>
