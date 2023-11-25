import dao

# user = {'name':'竹島','score':999999}

# dao.insert_one(user)
result = dao.find_all()
print(result)
print(result[0]['name'])