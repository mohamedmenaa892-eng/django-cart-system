# Shopping Cart System 

## 📌 Description

A Django-based shopping cart system that allows both authenticated and guest users to add products to a cart, manage item quantities, and remove items. The cart is maintained either via user accounts or session keys for non-logged-in users.

## 🚀 Features

* Add products to cart (AJAX-based)
* Support for authenticated and guest users
* Increase / decrease item quantity
* Remove items from cart
* Automatic cart creation using user or session
* Real-time cart item count update without page reload

## 🧠 How it works

The system links a cart to either:

* a logged-in user, or
* a session key for anonymous users

When a user adds a product:

* The system checks if a cart exists; if not, it creates one.
* A `CartItem` is created or updated if it already exists.
* Quantities are managed at the item level.
* JavaScript uses `fetch()` to send requests and updates the cart count dynamically without reloading the page.

## 🧱 Models

* **Cart**: Represents a shopping cart. It can belong to a logged-in user or a session (guest user). It stores creation time and calculates total price via its items.

* **CartItem**: Represents a product inside a cart. It includes:

  * Reference to a product
  * Quantity of the product
  * Unique constraint to prevent duplicate product entries per cart
  * A computed total price per item

## ⚙️ Key Functionality

* **Adding items to cart**

  * Uses `add_to_cart` view
  * Creates or updates a `CartItem`
  * Increases quantity if item already exists

* **Updating quantity**

  * `increase_item` increases quantity (limited by available product stock)
  * `decrease_item` decreases quantity (minimum is 1)

* **Removing items**

  * `remove_cartitem` deletes the item from the cart

* **Cart retrieval**

  * `get_user_cart` ensures a cart is always available for both authenticated and guest users

* **AJAX cart update**

  * `no_reload.js` sends POST requests using `fetch`
  * Updates cart count dynamically without page reload

## 🛠 Tech Stack

* Django
* HTML
* Bootstrap
* JavaScript (Fetch API, AJAX)

## 📂 Project Structure (optional)

* **views.py** → Contains cart logic (add, remove, update, retrieve cart)
* **models.py** → Defines Cart and CartItem database models
* **urls.py** → Routes for cart actions
* **admin.py** → Admin interface configuration for Cart and CartItem
* **no_reload.js** → Handles AJAX requests for adding items without reloading

## ▶️ How to run

* Install dependencies:

```bash
pip install -r requirements.txt
```

* Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

* Create a superuser:

```bash
python manage.py createsuperuser
```

* Start the development server:

```bash
python manage.py runserver
```

* Open in browser:

```
http://127.0.0.1:8000/
```

## 📝 Notes

* The cart supports both authenticated users and session-based anonymous users.
* A unique constraint ensures that each product appears only once per cart.
* AJAX is used to improve user experience by avoiding full page reloads when adding items.
* Stock validation is applied when increasing item quantity.
* The system assumes the `Product` model exists in the `stor` app with fields like `price` and `quantity`.

---
