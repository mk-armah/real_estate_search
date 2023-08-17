import pymongo
import urllib.parse
import dotenv

dotenv.load_dotenv()
import os


def connect_to_mongodb(database_name, collection_name):
    try:
        username = urllib.parse.quote_plus(os.getenv("DOCKER_MONGODB_USERNAME")) 
        password = urllib.parse.quote_plus(os.getenv("DOCKER_MONGODB_PWD"))
        host = os.getenv("DOCKER_MONGO_HOST")
        port = os.getenv("DOCKER_MONGO_PORT")
        
        connection_string = f"mongodb://{username}:{password}@{host}:{port}/"
        client = pymongo.MongoClient(connection_string)
        
        db = client[database_name]
        collection = db[collection_name]
        print("Connected to MongoDB successfully!")
        return collection
    except pymongo.errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        return None

if __name__ == "__main__":
    # Replace 'your_database_name' and 'your_collection_name' with your desired database and collection names
    database_name = 'realestatebackend'
    collection_name = 'lake'
    
    collection = connect_to_mongodb(database_name, collection_name)
    if collection is not None:
        data = {"name": "John Doe", "age": 30, "city": "New York"}
        result = collection.insert_one(data)
        print("Document inserted with ID:", result.inserted_id)
