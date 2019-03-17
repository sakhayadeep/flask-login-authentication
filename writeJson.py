import json

def writejson(dt, filename):
    try:
        with open(filename) as jfile:
            d = json.load(jfile)
            for user in d['users']:
                dt['users'].append(user)

        with open(filename, 'w') as jfile:
            json.dump(dt, jfile)

    except:
        with open(filename, 'w') as jfile:
            json.dump(dt, jfile)

if __name__ == '__main__':
    user = input("Insert username : ")
    password = input("Insert password : ")
    email = input("Insert email : ")
    degree = input("Insert degree : ")
    register = int(input("Insert register number : "))
    age = int(input("Insert age : "))
    city = input("Insert city : ")

    dt = {}
    dt['users'] = []
    dt['users'].append({"username": user, "password": password, "email": email, "degree": degree, "register": register, "age": age, "city": city})
    
    writejson(dt, 'data.json')
