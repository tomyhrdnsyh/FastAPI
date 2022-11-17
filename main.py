from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json


app = FastAPI()

with open('data.json') as file:
        data = json.load(file)

class Body(BaseModel):
    directed_by: str
    written_by: str
    
@app.get('/services/{episode}')
async def root(episode: str):

    if episode not in data:
        raise HTTPException(status_code=404, detail="Episode not found")

    response = {
        'status': 200,
        'message status': 'success',
        'data': data[episode]
    }
    return response

@app.post('/services/{id}')
async def edit(id:int, body: Body):
    key = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

    if id not in key.keys():
        raise HTTPException(status_code=404, detail="Id not found")
    
    data[key[id]]["Directed by"] = body.directed_by
    data[key[id]]["Written by"] = body.written_by

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    return data[key[id]]