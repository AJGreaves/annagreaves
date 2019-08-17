import os
from flask import Flask, redirect, render_template, request, url_for

# create instance of flask and assign it to "app"
app = Flask(__name__)

# Home page
@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)