from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Title

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/index')
def index():
	categories = session.query(Category).all()
	#titles = session.query(Title.filter_by(title_id=title.id))
	return render_template('index.html', categories=categories)
	#output = ''
	# for i in categories:
	# 	output += i.name
	# 	output += '</br>'
	# return output


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