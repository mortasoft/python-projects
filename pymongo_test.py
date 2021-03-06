import pymongo
from random import randint

myclient = pymongo.MongoClient("mongodb+srv://admin:wUgwaaV10Xas5GGR@cluster0.2hkjo.mongodb.net/test?authSource=admin&replicaSet=atlas-s2vfi6-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
mydb = myclient["test"]

db=mydb.business

names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 501):
    business = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
    }
    #Step 3: Insert business object directly into MongoDB via insert_one
    result=db.reviews.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))


mycol = mydb["test"]

myquery = { "Número de Referencia": "237635" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)



