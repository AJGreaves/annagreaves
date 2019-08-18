import os
from flask import Flask, redirect, render_template, request, url_for

# create instance of flask and assign it to "app"
app = Flask(__name__)

# Home page
@app.route('/')
def home_page():
        return render_template(
                'index.html',
                active='home',
                title="Home")

# Contact page
@app.route('/contact')
def contact_page():
        return render_template(
                'contact.html',
                active='contact',
                title="Contact")

# Portfolio page
@app.route('/portfolio')
def portfolio_page():
        return render_template(
                'portfolio.html',
                active='portfolio',
                title="Portfolio")

@app.route('/portfolio/familyhub')
def portfolio_familyhub():
        return render_template(
                'projects/familyhub.html',
                active="portfolio",
                title="Portfolio | Family Hub")

@app.route('/portfolio/annagilhespy')
def portfolio_annagilhespy():
        return render_template(
                'projects/annagilhespy.html',
                active="portfolio",
                title="Portfolio | Anna Gilhespy")

@app.route('/portfolio/clinicalkey')
def portfolio_clinicalkey():
        return render_template(
                'projects/clinicalkey.html',
                active="portfolio",
                title="Portfolio | ClinicalKey")

if __name__ == '__main__':
        app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)