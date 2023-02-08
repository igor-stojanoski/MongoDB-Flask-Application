from cleanco import basename
import re
import pandas as pd
import pymongo
import sqlite3
import pymongo
from cryptography.fernet import Fernet
from config import connect_sqlite, connect_mongo, secret_key

conn = connect_sqlite()
    
fernet = secret_key()
    
mycol = connect_mongo()


def clean_name(row):
    """Clean company name from unwanted characters.

    Args:
        row (str): Company name string.

    Returns:
        str: Return string with cleaned company name.
    """
    comp_name = basename(re.sub(r"\(.*?\)|[-,@'\"]|,.*", "", row['name']).title()).replace(":", " ").replace("@", " ").replace(".", " ")
    cleaned_name = re.sub(r"\(.*?\)|[-,.@'\"]|\b\w{1,2}&\w{1,2}\b|,.*", lambda x: x.group(0).upper(), comp_name).replace("  ", " ")
    return cleaned_name


def filter_names():
        
    # Number of records used for iteration.
    chunksize = 10000

    cleaned_name_df = pd.DataFrame()
   
    # Iterate over the 'companies' table in chunks
    for df in pd.read_sql("SELECT * FROM companies", conn, chunksize=chunksize):
        # Apply the cleaning function to the 'name' column
        df['company_name_cleaned'] = df.apply(clean_name, axis=1)
        df['nace'] = df['nace'].astype('Int64').astype('string')
        # Concatenating the dataframe 'cleaned_name_df' with the dataframe 'df'
        cleaned_name_df = pd.concat([cleaned_name_df, df])


    list_to_mongo = []

    # Iterate over the 'companies' table in chunks
    for data in pd.read_sql("SELECT company_name_cleaned, id, country_iso, city, nace, website FROM companies", conn, chunksize=chunksize):
        sqlite_rows = data.to_dict()
        for i in range(chunksize):
            company_name_enc = fernet.encrypt(bytes(str(sqlite_rows['company_name_cleaned'][i]), 'utf-8'))
            country_iso_enc = fernet.encrypt(bytes(str(sqlite_rows['country_iso'][i]), 'utf-8'))
            city_enc = fernet.encrypt(bytes(str(sqlite_rows['city'][i]), 'utf-8'))
            nace_enc = fernet.encrypt(bytes(str(sqlite_rows['nace'][i]), 'utf-8'))
            website_enc = fernet.encrypt(bytes(str(sqlite_rows['website'][i]), 'utf-8'))
            
            sqlite_data = {"_id": f"{int(sqlite_rows['id'][i])}", str(company_name_enc): [str(country_iso_enc), str(city_enc), str(nace_enc), str(website_enc)]}
            
            # Append encrypted dict to the list "list_to_mongo" with "company_name_cleaned" as a key, and other records as values.
            list_to_mongo.append(sqlite_data)    
      
    # Delete all records from MongoDB collection(if exists).      
    mycol.delete_many({})
    # Insert encrypted data to MongoDB.
    mycol.insert_many(list_to_mongo)

    # Check if column "company_name_cleaned" is empty.
    check_column = pd.read_sql("SELECT company_name_cleaned FROM companies", conn)
    if pd.isnull(check_column['company_name_cleaned']).all():
        return cleaned_name_df.to_sql("companies", conn, if_exists='replace', index=False)
    
def to_mongo(test=0):  
    """Get encrypted records from MongoDB, decrypts them with Fernet and return a list of dicts.

    Args:
        test (int, optional): Int values from 0 - 20000. Defaults to 0.

    Returns:
        list: Return a list of dicts.
    """
    
    front_end = []   

    #Iterate over the MongoDB with an integer argument and decrypting with Fernet.
    for x in mycol.find().limit(test):
        _id = list(x.items())[0][1]
        comp_name = fernet.decrypt(bytes(list(x.items())[1:2][0][0][2:-1], 'utf-8')).decode('utf-8')
        country_iso = fernet.decrypt(bytes(list(x.items())[1][1][0][2:-1], 'utf-8')).decode('utf-8')
        city = fernet.decrypt(bytes(list(x.items())[1][1][1][2:-1], 'utf-8')).decode('utf-8')
        nace = fernet.decrypt(bytes(list(x.items())[1][1][2][2:-1], 'utf-8')).decode('utf-8')
        website = fernet.decrypt(bytes(list(x.items())[1][1][3][2:-1], 'utf-8')).decode('utf-8')
        
        #Append dict to the list "front_end" with "company_name_cleaned" as a key, and other records as values.
        front_end.append({comp_name: [{"id": int(_id), "country_iso": country_iso, "city": city, "nace": nace, "website": website}]})
        
    return front_end


def range_slider(range1=0, range2=20):
    """Get encrypted records from MongoDB with range as argument, decrypts them and return a list od dicts.

    Args:
        range1 (int, optional): Int value from 0 - 20000. Defaults to 0.
        range2 (int, optional): Int value from 0 - 20000. Defaults to 100.

    Returns:
        list: Return a list of dicts.
    """

    slider_list = []
    
    #Iterate over the MongDB with range as argument and decrypting with Fernet.
    for x in list(mycol.find())[range1:range2]:
        _id = list(x.items())[0][1]
        comp_name = fernet.decrypt(bytes(list(x.items())[1:2][0][0][2:-1], 'utf-8')).decode('utf-8')
        country_iso = fernet.decrypt(bytes(list(x.items())[1][1][0][2:-1], 'utf-8')).decode('utf-8')
        city = fernet.decrypt(bytes(list(x.items())[1][1][1][2:-1], 'utf-8')).decode('utf-8')
        nace = fernet.decrypt(bytes(list(x.items())[1][1][2][2:-1], 'utf-8')).decode('utf-8')
        website = fernet.decrypt(bytes(list(x.items())[1][1][3][2:-1], 'utf-8')).decode('utf-8')
    
        #Append dict to the list "slider_list" with "company_name_cleaned" as a key, and other records as values.
        slider_list.append({comp_name: [{"id": int(_id), "country_iso": country_iso, "city": city, "nace": nace, "website": website}]})
   
    return slider_list


filter_names()