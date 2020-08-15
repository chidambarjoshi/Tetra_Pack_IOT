import pymongo
import datetime
client = pymongo.MongoClient("mongodb+srv://chidu:chidu@cluster0-ccngx.mongodb.net/tetrapack?retryWrites=true&w=majority")
db=client.get_database('tetrapack')
now = datetime.datetime.now()
records=db.mfdtemp
records1=db.phdata
class md :
   def on_rec(self,id,data):
       print(id)
       print(data)
       datain=records.find_one({'id':id})
       if datain is None:
           ns={
                'id':id,
                'mfd':now
            }
           records.insert_one(ns)
       iddata=records1.find_one({'id':id})

       if iddata is None:
           ns={
                'id':id,
                'phvalue':data,
                'Lastdate':now
                }
           records1.insert_one(ns)
           print("data inserted in both collections")
       else:
           update={
                            'phvalue':data,
                            'Lastdate':now
                            }
           records1.update_one({'id':id},{'$set':update})
           print("data updated")

#obj = md()
#id='07'
#data='6.5'
#obj.on_rec(id,data)