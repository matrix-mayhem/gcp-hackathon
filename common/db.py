from google.cloud import firestore
from sqlalchemy import create_engine

firestore_db = firestore.Client()

engine = create_engine("postgresql+psycopg2://user:password@HOST:5432/db")