import pymongo
from pymongo import MongoClient
import string
import hypothesis as h
import hypothesis.strategies as hs
from faker import Faker
from datetime import datetime
import os
from imutils import paths


number = int(input("Enter the number: "))

client = MongoClient('localhost', 27017)


#client = MongoClient('mongodb://localhost:27017/')

db = client.add_database
collection = db.add_database


imagePaths = list(paths.list_images("images"))
l = os.listdir(path='images')
Name=[x.split('.')[0] for x in l]


fake = Faker()


def test():
    for i in range(number):
        post = { "Name": Name[i] ,
            "DOB": fake.date(pattern="%Y-%m-%d"),
            "Phone": fake.phone_number() ,
            "Rank":fake.numerify(text="##") ,
            "service_number": fake.numerify(text="#########") ,
            "company": fake.company() ,
            "unit": fake.numerify(text="###"),
            "remarks": fake.lexify(text="???????????????", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")  ,
            "Uploaded_Image": imagePaths[i] , # intead of choosing random function take out images one by one from directory
            "is_suspicious": fake.boolean(chance_of_getting_true=50),

        }

        data = db.data
        post_id = data.insert_one(post)

        db.list_collection_names()


test()
