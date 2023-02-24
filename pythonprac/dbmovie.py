from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.i9vkog7.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

target_star = db.movies.find_one({'title':'가버나움'})['star']

movies = list(db.movies.find({'star':target_star},{'_id':False}))
for a in movies:
    print(a)