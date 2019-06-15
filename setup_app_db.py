from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    u_id = Column(Integer, primary_key = True)
    u_name = Column(Text, nullable = False)
    email = Column(Text, nullable = False)
    picture = Column(Text)



class Category(Base):

    __tablename__ = 'categories'

    cat_id = Column(Integer, primary_key = True)
    cat_name = Column(Text, nullable = False)
    user_id = Column(Integer, ForeignKey('users.u_id'))
    user = relationship(User, backref='categories')


    @property
    def serialise(self):
        """Return object data in serialised format"""
        return{
        'name'    :self.cat_name,
        'id'      :self.cat_id
        }


class Title(Base):

    __tablename__ = 'titles'

    t_id = Column(Integer, primary_key = True)
    t_name = Column(Text, nullable =False)
    author_name = Column(Text)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.cat_id'))
    category = relationship(Category, backref=backref('titles', cascade='all, delete'))
    user_id = Column(Integer, ForeignKey('users.u_id'))
    user = relationship(User, backref='titles')

    @property
    def serialise(self):
        """Return object data in serialised format"""
        return{
        'name'           :self.t_name,
        'id'             :self.t_id,
        'description'    :self.description,
        'category'       :self.categories.cat_name
        }



engine = create_engine('sqlite:///book_catalog.db')
Base.metadata.create_all(engine)