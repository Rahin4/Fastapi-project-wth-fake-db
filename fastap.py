from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from typing import List
app=FastAPI()


users=[]

class userIn(BaseModel):
    id: int
    name: str
    email: str
    town: str

class userOut(BaseModel):
    id:int
    name:str
    town: str
fake_db: List[userOut]=[]
@app.post('/create', response_model=userOut)
def create_user(user:userIn):
    user_id=len(fake_db)+1

    new_user=userOut(
        id=user_id,
        name= user.name,
        town=user.town
    )
    fake_db.append(new_user)
    return new_user


@app.get("/users/", response_model=List[userOut])
def get_user(id: Optional[int]=None, name:Optional[str]=None):
    if id is not None:
        return [user for user in fake_db if user.id==id]
    if name is not None:
        return [user for user in fake_db if user.name.lower()==name.lower()]
    return fake_db



@app.put("/users/", response_model=userOut)
def update_user(
    updated_user: userIn,
    user_id: Optional[int] =None,
    name: Optional[str] =None
):
    if user_id is not None:
        for i , user in enumerate(fake_db):
            if user_id==user.id:
                new_user=userOut(
                    id=user_id,
                    name=update_user.name,
                    town= updated_user.town
                )
                fake_db[i]=new_user
                return new_user
            
    if name is not None:
        for i , user in enumerate(fake_db):
            if name.lower()==user.name.lower():
                new_user=userOut(
                    id=user.id,
                    name=updated_user.name,
                    town=updated_user.town,
                )
                fake_db[i]=new_user
                return new_user
    raise HTTPException(status_code=404, detail="User not found by ID or Name")

            


@app.delete("/users/{user_id}", response_model=dict)
def del_user(user_id:int):
    for i , user in enumerate(fake_db):
        if user_id== user.id:
            del fake_db[i]
            return {"message":f"{user_id} is deleted successfully"}
    return{"error":f"{user_id} is not found"}
        


