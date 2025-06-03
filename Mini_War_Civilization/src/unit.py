from abc import ABC,abstractmethod # lo importamos para generar clases abstractas
import math

class Unit(ABC):
    """Clase base abstracta para todas las unidades en el juego."""
    def __init__(self, name: str, unit_type: str, strength: int, defense: int, hp: int, total_hp: int):
        """
        Constructor de la clase Unit.

        Args:
            name (str): Nombre de la unidad.
            unit_type (str): Tipo de unidad.
            strength (int): Fuerza de la unidad.
            defense (int): Defensa de la unidad.
            hp (int): Puntos de vida actuales de la unidad.
            total_hp (int): Puntos de vida totales de la unidad.
        """
        self._name = name
        self._unit_type = unit_type
        self._strength = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp

    # generamos metodos abstractos para evitar que el usuario pueda generar unidades genericas

    @abstractmethod
    def effectiveness(self, strength: int) -> int:
        """
        Método abstracto para determinar la efectividad del ataque contra otra unidad.

        Args:
            opponent (Unit): Unidad oponente.
        """
        pass

    @property
    def name(self):
        # Property (getter) for the name
        return self._name

    @name.setter
    def name(self, value: str):
        # Setter for the name
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def unit_type (self):
        return self._unit_type

    @property
    def strength (self):
        return self._strength

    @strength.setter
    def strength (self, value: int):
        if  isinstance(value, int) and value >= 0:
            self._strength = value
        else:
            raise ValueError("Number must be higher than 0")

    @property
    def defense (self):
        return self._defense

    @defense.setter
    def defense (self, value: int):
        if  isinstance(value, int) and value >= 0:
            self._defense = value
        else:
            raise ValueError("Number must be higher than 0")
    @property
    def hp (self):
        return self._hp

    @hp.setter
    def hp (self, value: int):
        if value < 0:
            self._hp = 0
        else:
            self._hp = value

    @property
    def total_hp(self):
        return self._total_hp

    @total_hp.setter
    def total_hp(self, value: int):
        self._total_hp = value

    def is_debilitated(self) -> bool:
        """
        Verifica si la unidad está debilitada (hp = 0).

        Returns:
            bool: True si la unidad está debilitada, de lo contrario False.
        """
        if self.hp <= 0:
            return True
        else:
            return False

    def attack(self, opponent:'Unit') -> int:
        """
        Método abstracto para atacar a otra unidad.

        Args:
            opponent (Unit): Unidad oponente.
        """
        opponent.hp -= 1
        return 1

class Archer(Unit):

    """Clase que representa una unidad de tipo Archer."""
    def __init__(self, name: str, strength: int = 7, defense: int = 2, hp: int = 15, total_hp: int = 15, arrows: int = 5):
        """
        Constructor de la clase Archer.

        Args:
            name (str): Nombre de la unidad.
            strength (int): Fuerza de la unidad.
            defense (int): Defensa de la unidad.
            hp (int): Puntos de vida actuales de la unidad.
            total_hp (int): Puntos de vida totales de la unidad.
            arrows (int): Número de flechas.
        """
        super().__init__(name, unit_type='Archer', strength=strength, defense=defense, hp=hp, total_hp=total_hp)
        self.arrows = arrows

    def attack(self,opponent:'Unit'):
        """
        Ataca a otra unidad.

        Args:
            opponent (Unit): Unidad oponente.

        Returns:
            int: Daño infligido al oponente.
        """
        d_type = {'Cavalry':1.5,'Infantry':0.5,'Worker':1,'Archer':1}
        if self.arrows > 0 :
            f =  max(1,(d_type[opponent.unit_type] * self.strength) - opponent.defense)
            valor = int(f)
            self.arrows -= 1
            if valor > opponent.hp:
                valor = opponent.hp
                opponent.hp = 0
                return valor
            else:
                opponent.hp -= valor
            return valor
        else:
            opponent.hp -= 1
            return 1

    def is_debilitated(self):
        """hereda la funcion de la clase padre Unit"""
        return super().is_debilitated()

    def effectiveness(self, opponent:'Unit'):
        """
        Determina la efectividad del ataque contra otra unidad.

        Args:
            opponent (Unit): Unidad oponente.

        Returns:
            float: Efectividad del ataque.
        """
        if opponent.unit_type == 'Cavalry':
          return 1
        elif opponent.unit_type == 'Infantry':
          return -1
        elif opponent.unit_type == 'Worker' or 'Archer':
          return 0

    def __str__(self):
        resp = f'{self.name} ({self.unit_type}) Stats: ATT: {self.strength}, DEF: {self.defense}, HP: {self.hp}/{self.total_hp})'
        return resp


class Cavalry(Unit):
    """Clase que representa una unidad de tipo Cavalry."""
    def __init__(self, name: str, strength: int = 5, defense: int = 2, hp: int = 25, total_hp: int = 25, charge : int = 5):
        """
        Constructor de la clase Cavalry.

        Args:
            name (str): Nombre de la unidad.
            strength (int): Fuerza de la unidad.
            defense (int): Defensa de la unidad.
            hp (int): Puntos de vida actuales de la unidad.
            total_hp (int): Puntos de vida totales de la unidad.
            charge (int): Carga de la unidad.
        """
        super().__init__(name, unit_type='Cavalry', strength=strength, defense=defense, hp=hp, total_hp= total_hp)
        self.charge = charge

    def attack(self,opponent:'Unit'):
        """
        Ataca a otra unidad.

        Args:
            opponent (Unit): Unidad oponente.

        Returns:
            int: Daño infligido al oponente.
        """
        d_type = {'Cavalry':1,'Infantry':1.5,'Worker':1,'Archer':0.5}
        f =  max(1,(self.charge + d_type[opponent.unit_type] * self.strength) - opponent.defense)
        valor = int(f)
        if valor > opponent.hp:
                valor = opponent.hp
                opponent.hp = 0
        else:
            opponent.hp -= valor
        return valor

    def is_debilitated(self):
        return super().is_debilitated()

    def effectiveness(self,opponent:'Unit'):
        """
        Determina la efectividad del ataque contra otra unidad.

        Args:
            opponent (Unit): Unidad oponente.

        Returns:
            float: Efectividad del ataque.
        """
        if opponent.unit_type == 'Archer':
          return -1

        elif opponent.unit_type == 'Infantry':
          return 1

        elif opponent.unit_type == 'Worker' or 'Cavalry':
          return 0

    def __str__(self):
        resp = f'{self.name} ({self.unit_type}) Stats: ATT: {self.strength}, DEF: {self.defense}, HP: {self.hp}/{self.total_hp})'
        return resp

class Infantry(Unit):

    """Clase que representa una unidad de tipo Infantry."""

    def __init__(self, name: str, strength: int = 3, defense: int = 2, hp: int = 25, total_hp: int = 25, fury: int = 3):
        """
        Constructor de la clase Infantry.

        Args:
            name (str): Nombre de la unidad.
            strength (int): Fuerza de la unidad.
            defense (int): Defensa de la unidad.
            hp (int): Puntos de vida actuales de la unidad.
            total_hp (int): Puntos de vida totales de la unidad.
            fury (int): Furia de la unidad.
        """
        super().__init__(name, unit_type='Infantry', strength=strength, defense=defense, hp=hp, total_hp=total_hp)
        self.fury = fury

    def attack(self,opponent:'Unit'):
        """
        Ataca a otra unidad.

        Args:
            opponent (Unit): Unidad oponente.

        Returns:
            int: Daño infligido al oponente.
        """
        d_type = {'Cavalry':0.5,'Infantry':1,'Worker':1,'Archer':1.5}
        f =  max(1,(self.fury + d_type[opponent.unit_type] * self.strength) - opponent.defense)
        valor = int(f)
        if valor > opponent.hp:
                valor = opponent.hp
                opponent.hp = 0
        else:
            opponent.hp -= valor
        return valor



    def is_debilitated(self):
        return super().is_debilitated()

    def effectiveness(self,opponent:'Unit'):
        """
        Determina la efectividad del ataque contra otra unidad.

        Args:
            opponent (Unit): Unidad oponente.

        Returns:
            float: Efectividad del ataque.
        """
        if opponent.unit_type == 'Archer':
          return 1
        elif opponent.unit_type == 'Cavalry':
          return -1
        elif opponent.unit_type == 'Worker' or 'Infantry':
          return 0

    def __str__(self):
        resp = f'{self.name} ({self.unit_type}) Stats: ATT: {self.strength}, DEF: {self.defense}, HP: {self.hp}/{self.total_hp})'
        return resp

class Worker(Unit):

    """Clase que representa una unidad de tipo Worker."""

    def __init__(self, name: str, strength: int = 1, defense: int = 0, hp: int = 5, total_hp: int = 5):
        """
        Constructor de la clase Worker.

        Args:
            name (str): Nombre de la unidad.
            strength (int): Fuerza de la unidad.
            defense (int): Defensa de la unidad.
            hp (int): Puntos de vida actuales de la unidad.
            total_hp (int): Puntos de vida totales de la unidad.
        """
        super().__init__(name, unit_type='Worker', strength=strength, defense=defense, hp=hp, total_hp=total_hp)

    def effectiveness(self,opponent:'Unit'):
        """
        Determina la efectividad del ataque contra otra unidad.

        Args:
            opponent (Unit): Unidad oponente.

        Returns:
            float: Efectividad del ataque.
        """
        return -1
    def collect (self):
        """
        Recolecta recursos.

        Returns:
            int: Cantidad de recursos recolectados.
        """
        return int(10)
    def __str__(self):
        resp = f'{self.name} ({self.unit_type}) Stats: ATT: {self.strength}, DEF: {self.defense}, HP: {self.hp}/{self.total_hp})'
        return resp