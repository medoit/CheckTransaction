import sqlalchemy as db
engine = db.create_engine('postgresql+psycopg2://postgres:1@localhost/postgres')

metadata = db.MetaData()

data_sub = db.Table('data_sub', metadata,
    db.Column('id', db.Integer, primary_key=True),
    

)