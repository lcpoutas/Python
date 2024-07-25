"""
    Desarrolla un sistema para una aerolínea que permita administrar vuelos y reservaciones. 
    Utiliza herencia para diferenciar entre diferentes tipos de aviones, y polimorfismo en los 
    métodos para agregar pasajeros a los vuelos, dependiendo de la clase de boleto que compran 
    (e.g., primera clase, clase económica).

    Objetivos:

    · Implementar clases para Avion, Vuelo, y Pasajero.
    · Extender la clase Vuelo para diferentes tipos de vuelos.
    · Usar encapsulación para proteger los datos de cada clase.
"""

import logging
import re

#configuracion del logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class Avion:
    
    def __init__(self, modelo, cap_total, cap_primera, cap_turista, Id, autonomia, fab_year):
        self._modelo = modelo
        self._cap_total = cap_total
        self._cap_primera = cap_primera
        self._cap_turista = cap_turista
        self._Id = Id
        self._autonomia = autonomia
        self._fab_year = fab_year
        self.check_capacity()
        
    def check_capacity(self):
        if self._cap_total < self._cap_turista+self._cap_primera:
            logger.error("Las capacidades están mal definidas, capacidad de primera + turista > capacidad total")
            raise ValueError("Las capacidades están mal definidas, capacidad de primera + turista > capacidad total")
        elif self._cap_total > self._cap_turista+self._cap_primera:
            logger.error("Las capacidades están mal definidas, capacidad de primera + turista < capacidad total")
            raise ValueError("Las capacidades están mal definidas, capacidad de primera + turista < capacidad total")
        
    @property
    def modelo(self):
            return self._modelo
        
    @modelo.setter
    def modelo(self, value):
        patron = re.compile(r"^[A-Za-z]+-?\d+$")
        if patron.match(value):
            self._modelo = value
        else:
            logger.error("El modelo introducido no es valido")
            raise ValueError("El modelo introducido no es valido")
        
    @property
    def cap_total(self):
        return self._cap_total
        
    @cap_total.setter
    def cap_total(self, value):
        if not isinstance(value, (int)):
            logger.error("la capacidad total ha de ser un número")
            raise ValueError("la capacidad total ha de ser un número")
        elif value <= 0:
            logger.error("la capacidad total ha de ser positiva")
            raise ValueError("la capacidad total ha de ser positiva")
        else:
            self._cap_total = value
                
    @property
    def cap_primera(self):
        return self._cap_primera
        
    @cap_primera.setter
    def cap_primera(self, value):
        if not isinstance(value, (int)):
            logger.error("la capacidad total ha de ser un número")
            raise ValueError("la capacidad total ha de ser un número")
        elif value <= 0:
            logger.error("la capacidad total ha de ser positiva")
            raise ValueError("la capacidad total ha de ser positiva")
        elif value >= self._cap_total:
            logger.error("La capacidad de primera clase no puede ser superior a la total")
            raise ValueError("La capacidad de primera clase no puede ser superior a la total")
        else:
            self._cap_primera = value
                
    @property
    def cap_turista(self):
        return self._cap_turista
        
    @cap_turista.setter
    def cap_turista(self, value):
        if not isinstance(self._cap_turista, (int)):
            logger.error("la capacidad total ha de ser un número")
            raise ValueError("la capacidad total ha de ser un número")
        elif value <= 0:
            logger.error("la capacidad total ha de ser positiva")
            raise ValueError("la capacidad total ha de ser positiva")
        elif value >= self._cap_total:
            logger.error("La capacidad de primera clase no puede ser superior a la total")
            raise ValueError("La capacidad de primera clase no puede ser superior a la total")
        else:
            self._cap_turista = value
        
    @property
    def Id(self):
        return self._Id
        
    @Id.setter
    def Id(self, value):
        patron = re.compile(r"^[A-Za-z0-9.-]{5,20}$")
        if patron.match(value):
            self._Id = value
        else:
            logger.error("El Id introducido no es valido")
            raise ValueError("El Id introducido no es valido")
                
    @property
    def autonomia(self):
        return self._autonomia
        
    @autonomia.setter
    def autonomia(self, value):
        if not isinstance(value, (int, float)):
            logger.error("la capacidad total ha de ser un número")
            raise ValueError("la capacidad total ha de ser un número")
        elif value <= 0:
            logger.error("la capacidad total ha de ser positiva")
            raise ValueError("la capacidad total ha de ser positiva")
        else:
            self._autonomia = value
                
    @property
    def fab_year(self):
        return self._fab_year
        
    @fab_year.setter
    def fav_year(self, value):
        if not isinstance(value, (int)):
            logger.error("la capacidad total ha de ser un número")
            raise ValueError("la capacidad total ha de ser un número")
        elif value <= 0:
            logger.error("la capacidad total ha de ser positiva")
            raise ValueError("la capacidad total ha de ser positiva")
        else:
            self._fab_year = value
                
                
    def __str__(self):
        
        #Imprime la información del modelo
        
        return (f"---- Aircraft Information ---- \n"
                f"Model: {self._modelo} \n"
                f"Total Capacity: {self._cap_total} passengers \n"
                f"First Class Capacity: {self._cap_primera} passengers \n"
                f"Economy Class Capacity: {self._cap_turista} passengers \n"
                f"ID: {self._Id} \n"
                f"Range: {self._autonomia} km \n"
                f"Year of Manufacture: {self._fab_year}")

class Vuelo():
    
    def __init__(self, Id, origen, destino, hora_salida, duracion):
        self._Id =Id
        self._origen = origen
        self._destino = destino
        self._hora_salida = hora_salida
        self._duracion = duracion
        self.__tipo_vuelo = None
        self._tax = None
        self._servicios = []

    @property
    def Id(self):
        return self._Id
    
    @Id.setter
    def Id(self, value):
        patron=re.compile(r"^[A-Za-z0-9.-]{5-20}$")
        if patron.match(value):
            self._Id = value
        else:
            logger.error("El numero de vuelo es incorrecto")
            
    @property
    def hora_salida(self):
        return self._hora_salida
    
    @hora_salida.setter
    def hora_salida(self, value):
        patron=re.compile(r"^(?:[01]\d|2[0-3])[:.][0-5]\d$")
        if patron.match(value):
            self._hora_salida= value
        else:
            logger.error("La hora introducida no es valida")
            
    @property
    def duracion(self):
        return self._duracion
    
    @duracion.setter
    def duracion(self, value):
        patron=re.compile(r"^(?:[01]\d|2[0-3])[:.][0-5]\d$")
        if patron.match(value):
            self._duracion= value
        else:
            logger.error("La duracion introducida no es valida")
    
    @property
    def tax(self):
        return self._tax

    def update_tax(self):
        #establecemos un polimorfismo dependiendo del tipo de vuelo
        if self.__tipo_vuelo == "nacional":
            self._tax = 0.05
        else:
            self._tax = 0.15
            
    @property
    def servicios(self):
        return self._servicios
    
    def update_servicios(self):
        #establecemos un polimorfismo dependiendo del tipo de vuelo (overloading)
        if self.__tipo_vuelo == "nacional":
            self._servicios = ["bebidas", "snacks"]
        else:
            self._servicios = ["Comida completa", "Peliculas", "kits confort", "seleccion bebidas premium"]
            
    def __str__(self):
        
        return (f"---- Información del vuelo ---- \n"
                f"Id: {self._Id} \n"
                f"Origen: {self._origen} \n"
                f"Destino: {self._destino} \n"
                f"Hora de salida: {self._hora_salida} h \n"
                f"Duracion: {self._duracion} h \n"
                f"Tipo de vuelo: {self.__tipo_vuelo} \n"
                f"Tasas: {self._tax} \n"
                f"Servicios: {self._servicios}")
            
class Nacional(Vuelo):
    
    def __init__(self, Id, origen, destino, hora_salida, duracion):
        super().__init__(Id, origen, destino, hora_salida, duracion)
        self.__tipo_vuelo = "nacional"
        self.update_tax() #polimorfismo del método update tax
        self.update_servicios()
        
    ciudades = ["madrid", "barcelona", "valencia", "sevilla", "málaga", "bilbao", "alicante", "gran canaria", 
                "tenerife", "palma de mallorca", "ibiza", "menorca", "lanzarote", "fuerteventura", "girona", 
                "santiago de compostela", "vigo", "a coruña", "zaragoza","asturias", "santander", "valladolid", 
                "pamplona", "san sebastián", "burgos", "león", "salamanca", "badajoz", "logroño", "la rioja", 
                "jerez", "murcia", "almería", "reus", "toledo", "huesca", "cádiz", "castellón", "ciudad real", 
                "córdoba", "granada", "guadalajara", "huelva", "jaén", "lugo", "ourense", "segovia", "soria", 
                "teruel", "toledo"]
        
    @property
    def origen(self):
        return self._origen
    
    @origen.setter
    def origen(self, value):
        if value.lower() in Nacional.ciudades:
            self._origen = value
        else:
            logger.error("El origen introducido no es valido")
            
    @property
    def destino(self):
        return self._origen
    
    @destino.setter
    def destino(self, value):
        if value.lower() not in Nacional.ciudades:
            logger.error("El origen introducido no es valido")
        elif value.lower() == self._origen:
            logger.error("El destino no puede ser el mismo que el origen")
        else:
            self._destino = value
            
    @property
    def tipo_vuelo(self):
        return self.__tipo_vuelo
            
        
class Inernacional(Vuelo):
    
    def __init__(self, Id, origen, destino, hora_salida, duracion):
        super().__init__(Id, origen, destino, hora_salida, duracion)
        self._tipo_vuelo = "internacional"
        self.update_tax() #polimorfismo del método update tax
        self.update_servicios()
    
    ciudades = ["new york", "london", "paris", "tokyo", "dubai", "los angeles", "hong kong", "singapore", "shanghai",
                "bangkok", "amsterdam", "sydney", "frankfurt", "beijing", "mumbai", "istanbul", "sao paulo", 
                "toronto", "kuala lumpur", "madrid", "bacelona", "sevilla", "valencia"]

    @property
    def origen(self):
        return self._origen
    
    @origen.setter
    def origen(self, value):
        if value.lower() in Internacional.ciudades:
            self._origen = value
        else:
            logger.error("El origen introducido no es valido")
            
    @property
    def destino(self):
        return self._origen
    
    @destino.setter
    def destino(self, value):
        if value.lower() not in Nacional.ciudades:
            logger.error("El origen introducido no es valido")
        elif value.lower() == self._origen:
            logger.error("El destino no puede ser el mismo que el origen")
        else:
            self._destino = value    
