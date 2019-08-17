import os
from flask import Flask, redirect, render_template, request, url_for

# create instance of flask and assign it to "app"
app = Flask(__name__)

# Home page
@app.route('/')
def home_page():
    return render_template(
        'index.html',
        active='home')

# Contact page
@app.route('/contact')
def contact_page():
    return render_template(
        'contact.html',
        active='contact')

@app.route('/portfolio')
def portfolio_page():
    return render_template(
        'portfolio.html',
        active='portfolio')


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)