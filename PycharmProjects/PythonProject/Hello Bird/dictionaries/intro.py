#set dictionary

customer ={
    "name": "John Smith",
    "age": 30,
    "is_verified:": True
}

print(customer["name"])
print(customer.get("birtdate", "Oct,8,1989")) #setting a default value

#update value
customer["name"] ="jack Smith"
print(customer["name"])

#add key value pair
customer["birth"] ="Jan,1,1999"
print(customer)
