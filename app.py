from fastapi import FastAPI
from ListOfPosts import ListOfPosts

app = FastAPI()

allLists = ListOfPosts.listOfPosts()

@app.get("/")
def getAllLists():
    return allLists