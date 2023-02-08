import sqlite3
import pymongo
from cryptography.fernet import Fernet

def connect_mongo():
    #MongoDB connection details
    myclient = pymongo.MongoClient('mongodb://mongdbuser:123456@127.0.0.1:27017/')
    mydb = myclient['flaskapp']
    mycol = mydb['companies']
    return mycol

def connect_sqlite():
    # Connect to the SQLite database
    conn = sqlite3.connect('semos_companies_data.db', check_same_thread=False)
    return conn

def secret_key():
    #Fernet key fro encryption and decryption
    key = b'zK9GRh1Te8bn8_pWi9q4N_YY5l_YTYn1SXAFrW2H318='
    fernet = Fernet(key)
    return fernet
