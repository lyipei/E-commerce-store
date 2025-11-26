# Overview

This project is a dynamic e-commerce web application built using Django. The app allows users to browse products, add items to a shopping cart, and complete checkout.

The purpose of this project was to strengthen software engineering skills in building interactive web appswith CRUD-style functionality, server-side rendering, and basic data management. It also demonstrates real world practices such as separating business logic, validating inputs, and organizing templates and static files.

To run the project locally, start the Django development server with:

```bash
python manage.py runserver
```
Then, open the web browser and navigate to:
```cpp
http://127.0.0.1:8000/
```
This will display the product listing page, the main entry point of the app.


[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

* Product List page

Display all available products in a grid layout. Each product shows its name, price, description, and an "Add to Cart" button. Content is dynamically generated from the product database. User can click on "Add to Cart" to add items.

* Shopping Cart page

Shows all items in the user's cart with quantity and total price. Users can continue shopping or proceed to checkout. The page dynamically calculates totals based on items in the cart.

* Checkout page

Users input their name, email, and shipping address. Submitting the form clears the cart and redirects to the success page. The page dynamically calculated the total cost of the items.

* Checkout Success page

Confirms the order, showing the customer's name and total amount. Content is dynamically generated from user input submitted on the checkout page.

# Development Environment

1. Programming Language: Python 3.14
2. Framework: Django 5.2.8
3. Libraries: Django ORM, Django templating, CSS for styling
4. Tools: VS Code

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Django documentation](https://docs.djangoproject.com/en/5.2/)
* [Django Tutorial](https://docs.djangoproject.com/en/5.2/)

# Future Work

* Add user authentication so user can save carts and track order history
* Improve input validation and error handling with consistent responses and status codes.