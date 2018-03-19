from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import json
import re

if 'VCAP_SERVICES' in os.environ:
    services = json.loads(os.getenv('VCAP_SERVICES'))
    mysql_uri = json.dumps(services['p-mysql'][0]['credentials']['uri']).strip('"');
    mysql_uri = re.sub('\?reconnect=true', '', mysql_uri )
else:
    mysql_uri = dict(hostname='localhost', port=3306, password='')


engine = create_engine(mysql_uri, echo=True)

#engine = create_engine('mysql://root:zaq12wsx@localhost:13306/flask_test?charset=utf8', echo=True)
# engine = create_engine('mysql://SzFDPabFVHP0nEDG:eobT5Juig4wIwRgY@10.0.16.54:3306/cf_2fdf21fb_7af5_47b9_a75f_06eb18d63f2c?reconnect=true', echo=True)

# mysql://SzFDPabFVHP0nEDG:eobT5Juig4wIwRgY@10.0.16.54:3306/cf_2fdf21fb_7af5_47b9_a75f_06eb18d63f2c


DB_Session = sessionmaker(bind=engine)
db_session = DB_Session()
Base = declarative_base()


def init_db():
    print('tetttttt')
    print(mysql_uri)
    import models
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(engine)


def initial_db():
    # drop_db()
    init_db()


if __name__ == '__main__':
    init_db(engine)
