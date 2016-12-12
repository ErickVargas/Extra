import json

class Clientes:  
    data = []

    def read(self):
        with open('clientes.json','r') as file:
            data = json.load(file)
            self.data = data['results'] 

    def getClientes(self): 
        clientes = []
        for row in self.data:
            cliente = row['nombre']
            if cliente not in clientes:
                clientes.append(cliente)
        return clientes

    
                
class Peliculas:  
    data1 = []

    def read(self):
        with open('peliculas.json','r') as file:
            data1 = json.load(file)
            self.data1 = data1['results'] 

    def getPeliculas(self): 
        peliculas = []
        for row in self.data1:
            pelicula = row['nombre']
            if pelicula not in peliculas:
                peliculas.append(pelicula)
        return peliculas