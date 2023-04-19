## 3. Dado un texto con una lista de ciudades con su emblema mas importante, pedir las ciudades para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema. **Nota** el diccionario deberá ordenarse por su clave
def principal():
    cityEmblem = {
        'New York': 'The Statue of Liberty',
        'Tokyo': 'The cherry blossom',
        'Paris': 'The Eiffel Tower',
        'London': 'Big Ben',
        'Sydney': 'The Sydney Opera House',
        'Buenos Aires': 'The Obelisk',
        'Johannesburg': 'The Lion',
        'Moscow': 'The Kremlin',
        'Amsterdam': 'The windmills',
        'Dubai': 'The Burj Khalifa'
    }
    cities = input("Enter the cities separated by commas: ").split(',')

    result = {}
    for city in cities:
        city = city.strip()
        if city in cityEmblem:
            result[city] = cityEmblem[city]

    # result = {city.strip(): cityEmblem[city.strip()] for city in cities if city.strip() in cityEmblem}

    result = dict(sorted(result.items()))

    print(result)

if __name__=="__main__":
    principal()