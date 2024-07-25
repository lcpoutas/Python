"""
    Diseña una clase Notificacion y varias subclases como Email, SMS, y 
    NotificacionApp.
    
    Cada subclase debe tener un método enviar() que funcione de manera 
    diferente dependiendo del tipo de notificación
"""

from abc import ABC, abstractmethod

# configuramos el sistema de notificación de errores
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Notificacion(ABC):
    
    def __init__(self, mensaje):
        self.__tipo = None # se define en la subclase
        self.mensaje=mensaje
        
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        if tipo in ["sms", "mail", "app"]:
            self._tipo=tipo
        else:
            logger.error("El tipo de notificación no es valido")
            raise ValueError("El tipo de notificación no es valido")
            
    @abstractmethod
    def enviar(self):
        # Método abstracto para enviar notificaciones 
        # que debe ser implementado por cada subclase
        pass
    
class Sms(Notificacion):
    
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.tipo="sms"
    
    def enviar(self):
        logger.info(f"El mensaje se ha enviado por SMS correctamente")
        print(self.mensaje)
        
class Email(Notificacion):
    
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.tipo="mail"
    
    def enviar(self):
        logger.info(f"El mensaje se ha enviado por Email correctamente")
        print(self.mensaje)
        
class App(Notificacion):
    
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.tipo="app"
    
    def enviar(self):
        logger.info(f"El mensaje se ha enviado por App correctamente")
        print(self.mensaje)

