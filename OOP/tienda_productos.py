"""
Tienda de Productos:

    Crea una clase Producto con métodos para aplicar_descuento() y 
    calcular_precio().

    Extiende esta clase en ProductoAlimenticio, ProductoElectronico, etc., 
    modificando el método de descuento según el tipo de producto.

"""

# importar modulos necesarios
from abc import ABC, abstractmethod
import logging

#configurar el logging
logging.basicConfig(level=logging.ERROR)
logger=logging.getLogger(__name__)

class Producto(ABC):
    
    def __init__(self, producto, precioBase):
        if not isinstance(producto,str):
            logger.error("Error al establecer el producto")
            raise ValueError("EL producto debe ser un string")
        self._producto=producto
        print("El producto se ha establecido correctamente")

        if not isinstance(precioBase,(int, float)) or precioBase<0:
            logger.error("Error al establecer el precio")
            raise ValueError("EL precio debe ser un número positivo")
        self._precioBase = precioBase
        print("El precio del producto se ha establecido correctamente")
            
        self.descuento = 0
        self.precioFinal= None
        
    @property
    def producto(self):
        return self._producto
        
    @producto.setter
    def producto(self, producto):
        if not isinstance(producto,str):
            logger.error("Error al establecer el producto")
            raise ValueError("EL producto debe ser un string")
        self._producto=producto
        print("El producto se ha establecido correctamente")
            
    @property
    def precioBase(self):
        return self._precioBase
        
    @precioBase.setter
    def precioBase(self, precioBase):
        if not isinstance(precioBase,(int, float)) and precioBase>0:
            self._precioBase=precioBase
            print("El precio del producto se ha establecido correctamente")
        else:
            logger.error("Error al establecer el precio")
            raise ValueError("EL precio debe ser un número positivo")
        
    @abstractmethod
    def aplicar_descuento(self):
        #calcula el descuento dependiendo del tipo de producto
        pass
    
    def calcular_precio(self):

        self.precioFinal = self._precioBase - self.descuento
        print(f"El precio final es: {self.precioFinal} euros")
        return self.precioFinal
        
class ProductoAlimenticio(Producto):
    
    def aplicar_descuento(self):
        # Apply a 5% discount for food products
        self.descuento = 0.05 * self._precioBase
        print(f"El descuento aplicado es de: {round(self.descuento, 2)} euros")
        
class ProductoElectronico(Producto):
    
    def aplicar_descuento(self):
        # Apply a 15% discount for food products
        self.descuento = 0.15 * self._precioBase
        print(f"El descuento aplicado es de: {round(self.descuento, 2)} euros")    
