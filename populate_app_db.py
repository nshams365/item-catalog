from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setup_app_db import Title, User, Base

engine = create_engine('sqlite:///book_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy title
user1 = User(u_name="Noor Shams", email="nshams365@gmail.com", picture="https://media.licdn.com/dms/image/C4D03AQFzLp_GzKOEmw/profile-displayphoto-shrink_200_200/0?e=1565827200&v=beta&t=Rbr-v9IMIxCNfIXdT_bN-0ZY6BFZhIay7fzid-HHmWo")
session.add(user1)
session.commit()

# Titles table entry

title2 = Title(t_name="isms Understanding Art",
	author_name= "Stephen Little",
	description= "A handy guide to a wide range of art 'isms'. Herbert Press London.",
	category_id=1,
	user_id=1)
session.add(title2)
session.commit()

title3 = Title(t_name="Grow Your Own Crops in Pots",
	author_name= "Kay Maguire",
	description= "30 steps by step projects using vegetables, fruit and herbs.",
	category_id=3,
	user_id=1)
session.add(title3)
session.commit()

title4 = Title(t_name="Bad Science",
	author_name= "Ben Goldacre",
	description= "A brilliant book that debunks medical nonsense",
	category_id=13,
	user_id=1)
session.add(title4)
session.commit()


title5 = Title(t_name="The Naked Trader",
	author_name= "Robbie Burns",
	description= "How anyone can make money trading shares.",
	category_id=13,
	user_id=1)
session.add(title5)
session.commit()

title6 = Title(t_name="Digital Fortress",
	author_name= "Dan Brown",
	description= " ",
	category_id=21,
	user_id=1)
session.add(title6)
session.commit()


title7 = Title(t_name="To Kill a Mockingbird",
	author_name= "Harper Lee",
	description= "",
	category_id=23,
	user_id=1)
session.add(title7)
session.commit()

title8 = Title(t_name="Fifteen Poets",
	author_name= "Various",
	description= "The best work of the greate masters of English poetry from Chaucer to Matthew Arnold.",
	category_id=19,
	user_id=1)
session.add(title8)
session.commit()

title9 = Title(t_name="Chings Fast Food",
	author_name= "Ching-He Huang",
	description= "110 quick and healthy Chinese favorites.",
	category_id=27,
	user_id=1)
session.add(title9)
session.commit()

title10 = Title(t_name="The Joy of Less",
	author_name= "Francine Jay",
	description= "A minimalist guide to declutter, organize and simplify.",
	category_id=29,
	user_id=1)
session.add(title10)
session.commit()
