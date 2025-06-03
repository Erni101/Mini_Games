from abc import ABC,abstractmethod # lo importamos para generar clases abstractas
import Mini_War_Civilization.src.unit as unit

class Civilization ():
    """Clase que representa una civilización en el juego."""
    def __init__(self,name:str ,resources:int,units:list):
        """
        Constructor de la clase Civilization.

        Args:
            name (str): Nombre de la civilización.
            resources (int): Cantidad inicial de recursos.
            units (list): Lista de unidades iniciales.
        """
        self.name = name
        self.resources = resources
        self.units = units
        self.contador = {"Archer": 0, "Cavalry": 0, "Infantry": 0, "Worker": 0}


    def __str__(self):
        """
        Devuelve una representación en cadena de la civilización.

        Returns:
            str: Representación en cadena de la civilización.
        """
        resp = f'Nombre de la Civilizacion : {self.name} \n'
        resp += f'\t Recursos: {self.resources} \n'
        resp += f'\t Unidades: {self.units}'

        return resp

    def train_unit(self, unit_type: str):
        """
        Entrena una nueva unidad del tipo especificado.

        Args:
            unit_type (str): Tipo de unidad a entrenar ("Archer", "Cavalry", "Infantry", "Worker").
        """
        nuevo = None
        if unit_type in ["Archer", "Cavalry", "Infantry"]:
            if self.resources >= 60:
                self.resources -= 60
                self.contador[unit_type] += 1
                cuenta = self.contador[unit_type]
                if unit_type == "Archer":
                    nuevo = unit.Archer(name=unit_type + "_" + str(cuenta))
                elif unit_type == "Infantry":
                    nuevo = unit.Infantry(name=unit_type + "_" + str(cuenta))
                elif unit_type == "Cavalry":
                    nuevo = unit.Cavalry(name=unit_type + "_" + str(cuenta))
            else:
                print("None")
        elif unit_type == "Worker":
            if self.resources >= 30:
                self.resources -= 30
                self.contador[unit_type] += 1
                cuenta = self.contador[unit_type]
                nuevo = unit.Worker(name=unit_type + "_" + str(cuenta))
            else:
                print("None")

        if nuevo is not None:
            self.units.append(nuevo)


    def collect_resources(self):
        """
        Recolecta recursos de los trabajadores (Worker) de la civilización.

        Returns:
            int: Cantidad total de recursos después de la recolección.
        """
        for trabajadores in self.units:
            if trabajadores.unit_type == 'Worker' and trabajadores.hp != 0:
                x = trabajadores.collect()
                self.resources += x
        return self.resources

    def all_debilitated(self):
        """
        Verifica si todas las unidades de la civilización están debilitadas (hp = 0).

        Returns:
            bool: True si todas las unidades están debilitadas, de lo contrario False.
        """
        for vivos in self.units:
            if vivos.hp != 0:
                return False
        return True