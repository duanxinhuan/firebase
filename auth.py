import configparser
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account

def getDb():
    conf = getConfig()
    cred = credentials.Certificate(conf["serviceAccount"])
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

def getConfig():
    con = configparser.ConfigParser()
    con.read('conf.ini')

    configDict = {
        "apiKey": con["api settings"]["apiKey"],
        "authDomain": con["api settings"]["authDomain"],
        "databaseURL": con["api settings"]["databaseURL"],
        "storageBucket": con["api settings"]["storageBucket"],
        "serviceAccount": con["api settings"]["serviceAccount"]
    }
    return configDict




if __name__ == "__main__":
    db = getDb()
    users_ref = db.collection(u'Users').stream()
    for doc in users_ref:
        
        print(f'{doc.id} => {doc.to_dict()}')  
        
