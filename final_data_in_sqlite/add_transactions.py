from sqlalchemy.orm import sessionmaker

from sqlite_shema import UsaGov, engine

Session = sessionmaker(bind=engine)
session = Session()

user = UsaGov()

new_record = UsaGov(
    web_browser='Mozilla/5.0',
    operating_sys='Windows NT 6.1; WOW64',
    from_url='http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf',
    to_url='http://www.ncbi.nlm.nih.gov/pubmed/22415991',
    city='Danvers',
    latitude=42.576698,
    longitude=-70.954903,
    time_zone='America/New_York',
    time_in='2012-03-25 20:10:30',  
    time_out='2012-03-25 20:30:37'  
)

session.add(new_record)
session.commit()

records = session.query(UsaGov).all()
