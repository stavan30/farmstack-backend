from model import Todo

#MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.TodoList
collection = database.todo

#get one todo
async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})

    return document

#get all todo
async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

#add todo
async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

#update todo
async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document

#delete todo
async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True    
