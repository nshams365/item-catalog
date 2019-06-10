from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
# user1 = User(name="Noor Shams", email="nshams365@gmail.com", picture="https://media.licdn.com/dms/image/C4D03AQFzLp_GzKOEmw/profile-displayphoto-shrink_200_200/0?e=1565827200&v=beta&t=Rbr-v9IMIxCNfIXdT_bN-0ZY6BFZhIay7fzid-HHmWo")
# session.add(user1)
# session.commit()

# Create category #1 and add items to the category
category1 = Category(name="Technology")

session.add(category1)
session.commit()

# item1 = Item(name="Programming with C",
#             description= "Learning C programming ",
#             author= "",
#             image = "/static/programming_with_c.jpg",
#             category=category1)
# session.add(item1)
# session.commit()

# Create category #2 and add items to the category
category2 = Category(name="Fiction")

session.add(category2)
session.commit()

# item2 = Item(name = "The Da Vinci Code",
#             description ="fiction",
#             author="Dan Brown",
#             image = "/static/the_da_vinci_code.jpg",
#             category=category2)
# session.add(item2)
# session.commit()

# item3 = Item(name="Digital Fortress",
#              description="fiction",
#              author="Dan Brown",
#              image = "/static/digital_fortress.jpg",
#              category=category2)
# session.add(item3)
# session.commit()

# Create category #3 and add items to the category
category3 = Category(name="Cook Book")

session.add(category3)
session.commit()

# item4 = Item(name="Ching's Fast Food",
#              description="Chineese food cooking",
#              author="Ching-He Huang"
#              # image = "/static/chings_fast_food.jpg",
#              category=category3)
# session.add(item4)
# session.commit()

# item5 = Item(name="The Dukan Diet",
#              description="Dukan diet meal preparation",
#              author="Dr Pierre Dukan"
#              # image = "/static/the_dukan_diet.jpg",
#              category=category3)
# session.add(item5)
# session.commit()

# Create category #4 and add items to the category
category4 = Category(name="Courseware")

session.add(category4)
session.commit()

# item6 = Item(name="Wavesphere Application Server v8.5",
#              description="Wavesphere application",
#              author= ""
#              # image = "/static/wavesphere_application.jpg",
#              category=category4)
# session.add(item6)
# session.commit()
