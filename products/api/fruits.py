from ninja import Router
from products.services import *




fruits_router = Router(tags=['fruits_endpoint'])


@fruits_router.get("/api/v1/fruits")
def get_all_fruits(request):
    fruits = FileReading()
    if fruits:
        return fruits
    return  "json file is EMPTY"



@fruits_router.get("/api/v1/fruits/:id")
def get_fruit(request, ID: int):
    
    fruits = FileReading()

    filtered_list = []

    for dictionary in fruits:
        if dictionary['id'] == ID:
            filtered_list.append(dictionary)
    
    
    if filtered_list:
        return filtered_list
    return "no match"
    
    


@fruits_router.post("/api/v1/fruits/")
def new_fruit(request, id: int, name: str, description: str):
    data = FileReading()
    temp = data
    
    new_data = {"id": id, "name": name, "description": description}
    temp.append(new_data)
        
    FileWritting(data)
    
    return data



@fruits_router.delete("/api/v1/fruits/:id")
def del_fruit(request, ID: int):
    
    fruits = FileReading()
    
    for key, value in enumerate(fruits):
        if value["id"] == ID:
            fruits.pop(key)  
            FileWritting(fruits)
            return fruits  
    
    return "no match"   