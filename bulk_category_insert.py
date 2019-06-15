from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setup_app_db import Category, Base

engine = create_engine('sqlite:///book_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
# user1 = User(name="Noor Shams", email="nshams365@gmail.com", picture="https://media.licdn.com/dms/image/C4D03AQFzLp_GzKOEmw/profile-displayphoto-shrink_200_200/0?e=1565827200&v=beta&t=Rbr-v9IMIxCNfIXdT_bN-0ZY6BFZhIay7fzid-HHmWo")
# session.add(user1)
# session.commit()

# Create category #1 and add items to the category

categories = [ "Art", "Crime", "Gardening", "Graphic Novels", "Romance", "Spirituality", "Biography", "Classics", "Ebooks", "Historical Fiction", "Memoir", "Philosophy", "Science", "Sports", "Business", "Comics", "History", "Music", "Poetry", "Science Fiction", "Thriller", "Textbooks", "Fiction", "Self Help", "Travel", "Children's", "Cookbooks", "Humor and Comedy", "Nonfiction", "Religion" ]

for i in categories:
	category = Category(cat_name= i)
	session.add(category)
	session.commit()

