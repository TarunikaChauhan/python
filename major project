from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.permanent_session_lifetime = timedelta(days=7)

# Database simulation
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 19.99},
    {"id": 3, "name": "Product 3", "price": 14.99},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def product_list():
    return render_template("products.html", products=products)

@app.route("/cart", methods=["GET", "POST"])
def cart():
    if request.method == "POST":
        product_id = int(request.form.get("product_id"))
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            if "cart" not in session:
                session["cart"] = []
            session["cart"].append(product)
            return redirect(url_for("cart"))
    return render_template("cart.html", cart=session.get("cart"))

@app.route("/checkout")
def checkout():
    if "cart" in session:
        cart_items = session["cart"]
        session.pop("cart")
        return render_template("checkout.html", cart_items=cart_items)
    return redirect(url_for("cart"))

if __name__ == "__main__":
    app.run(debug=True)
