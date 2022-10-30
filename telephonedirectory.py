import pymongo
import pprint as pp
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client['PhoneDir']
collection=db['Telephone']

#INSERTION OF 1 Telephone no with details

# custinfo={'Name':'Aaaaa','Phone_No':1111111111,'Locality':'Tambaram','Place':'Chennai','State':'TN'}
# insert_id=collection.insert_one(custinfo)
# print(insert_id.inserted_id)
# data=collection.find_one()
# print(data)
# INSERTION OF MANY FACULTY DATA
Customer_info=[
   {'Name':'Anish','Phone_No':9123465789,'City':'Chennai','State':'TN'},
   {'Name':'Akil','Phone_No':9876543221,'City':'Chennai','State':'TN'},
   {'Name':'Bobby','Phone_No':9871123466,'City':'Madurai','State':'TN'},
   {'Name':'Babu','Phone_No':9785164123,'City':'Trichy','State':'TN'},
   {'Name':'Chandra','Phone_No':9136524785,'City':'Coimbatore','State':'TN'},
   {'Name':'Das','Phone_No':9265874123,'City':'Guntur','State':'AP'},
   {'Name':'Dilli','Phone_No':7589641230,'City':'Tirupathi','State':'AP'},
   {'Name':'Rolex','Phone_No':9840212305,'City':'Bangalore','State':'KA'},
   {'Name':'Vikram','Phone_No':8256974123,'City':'Cantonment','State':'KA'},
   {'Name':'Sara','Phone_No':9741568231,'City':'Trivandrum','State':'KL'},
   {'Name':'Efa','Phone_No':8713240654,'City':'Cochin','State':'KL'},
   {'Name':'Francis','Phone_No':9658743210,'City':'Hyderabad','State':'TS'},
   {'Name':'Garuda','Phone_No':9764523105,'City':'Ernakulam','State':'KL'},
   {'Name':'Hari','Phone_No':8312654970,'City':'Warangal','State':'TS'},
   {'Name':'Manche','Phone_No':7871056942,'City':'Nellore','State':'AP'},]
# ids=collection.insert_many(Customer_info)
# print(ids.inserted_ids)
print('---------------------QUERYING OPERATIONS---------------------')
query=db.Telephone.find({},{'_id':0,'Name':1,'Phone_No':1,'City':1,'State':1})
for i in query:
    print(i)
print('---------------------Find Specific Documents---------------------')
find1=db.Telephone.find({"State":'TN'})
for j in find1:
    pp.pprint(j)
print('---------------------SORTING OPERATIONS---------------------')
sort1=db.Telephone.find({},{'_id':0,'Name':1,'Phone_No':1,'City':1,'State':1}).sort("Name",1)
for k in sort1:
    print(k)

print('---------------------UPDATE OPERATIONS---------------------')
updat=db.Telephone.update_one({'Name':'Das'},{"$set":{'Name':"Dass"}})
print(updat)

print('------------UPDATE MANY-----------')
upmany=db.Telephone.update_many({'State':'TN'},{'$set':{'State':'Tamil Nadu'}})
print(upmany)


print('------------DELETE ONE-----------')
del1=db.Telephone.delete_one({'City':'Cantonment'})
print(del1)
for m in db.Telephone.find():
    pp.pprint(m)










