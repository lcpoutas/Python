import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class CuentaBancaria:
    
    def __init__(self, saldo=0):
        """Inicializa la cuenta con un saldo, que por defecto es 0."""
        self.__saldo = saldo
        
    @property
    def saldo(self):
        """Devuelve el saldo actual de la cuenta para consultas seguras."""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo=saldo
    
    def ingresar(self, amount):
        """Permite ingresar dinero en la cuenta. La cantidad debe ser positiva."""
        if amount < 0:
            logger.error(f"Intento fallido de ingreso: {amount} euros. La cantidad no puede ser negativa.")
            raise ValueError("No puedes introducir valores negativos")
        else:
            self.__saldo += amount
            logger.info(f"Ha ingresado {amount} euros. Saldo actual: {self.__saldo} euros")
        
    def retirar(self, amount):
        """Permite retirar dinero de la cuenta si la cantidad es positiva y hay fondos suficientes."""
        if amount < 0:
            logger.error(f"Intento fallido de retirada: {amount} euros. La cantidad no puede ser negativa.")
            raise ValueError("No puedes introducir valores negativos")
        elif self.__saldo < 0:
            logger.error("Intento de retirada con saldo negativo.")
            raise ValueError("No puedes sacar dinero, tu saldo está a cero")
        elif amount > self.__saldo:
            logger.error(f"Intento fallido de retirada: {amount} euros. No hay suficiente saldo.")
            raise ValueError("No puedes sacar más dinero que el disponible en tu saldo")
        else:
            self.__saldo -= amount
            logger.info(f"Ha retirado {amount} euros. Saldo actual: {self.__saldo} euros")

