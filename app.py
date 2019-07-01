#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Module Imports
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from setup_app_db import *

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Application instance
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

app = Flask(__name__)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Flask instance
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# DB connection
engine = create_engine('sqlite:///book_catalog.db')
Base.metadata.bind = engine

# Session instance 
DBSession = sessionmaker(bind=engine)
session = DBSession()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Application routing
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Application Home
@app.route('/')
@app.route('/library/')
def showLibrary():
	categories = session.query(Category).order_by(asc(Category.cat_name))
	titles = session.query(Title).order_by(desc(Title.t_id)).limit(5)
	return render_template('library.html', categories=categories, titles=titles)

# Books in a Category

@app.route('/library/<path:category_name>')
@app.route('/library/<path:category_name>/books/')
def showCategoryBooks(category_name):
	category = session.query(Category).filter_by(cat_name=category_name).one()
	titles = session.query(Title).filter_by(category=category).all()
	return render_template('books.html', category=category.cat_name, titles=titles)



# Book details



	

# @app.route('/categories/<int:category_id>/new/', methods=['GET','POST'])
# def newEntry(category_id):
# 	if request.method == 'POST':
# 		newEntry= Title(name = request.form['name'],category_id=category_id)
# 		session.add(newEntry)
# 		session.commit()
# 		return redirect(url_for('catalog', category_id=category_id))
# 	else:
# 		return render_template('newentry.html', category_id=category_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)