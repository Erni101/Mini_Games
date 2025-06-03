import unittest
import sys
import os

# Añade el directorio src al path para importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from unit import Archer, Cavalry, Infantry, Worker

class TestUnits(unittest.TestCase):
    def test_archer_creation(self):
        archer = Archer("Robin")
        self.assertEqual(archer.name, "Robin")
        self.assertEqual(archer.unit_type, "Archer")
        self.assertEqual(archer.strength, 7)
        self.assertEqual(archer.defense, 2)
        self.assertEqual(archer.hp, 15)
        self.assertEqual(archer.total_hp, 15)
        self.assertEqual(archer.arrows, 5)

    def test_cavalry_creation(self):
        cavalry = Cavalry("Maximus")
        self.assertEqual(cavalry.name, "Maximus")
        self.assertEqual(cavalry.unit_type, "Cavalry")
        self.assertEqual(cavalry.strength, 5)
        self.assertEqual(cavalry.defense, 2)
        self.assertEqual(cavalry.hp, 25)
        self.assertEqual(cavalry.total_hp, 25)
        self.assertEqual(cavalry.charge, 5)

    def test_infantry_creation(self):
        infantry = Infantry("Leonidas")
        self.assertEqual(infantry.name, "Leonidas")
        self.assertEqual(infantry.unit_type, "Infantry")
        self.assertEqual(infantry.strength, 3)
        self.assertEqual(infantry.defense, 2)
        self.assertEqual(infantry.hp, 25)
        self.assertEqual(infantry.total_hp, 25)
        self.assertEqual(infantry.fury, 3)

    def test_worker_creation(self):
        worker = Worker("Bob")
        self.assertEqual(worker.name, "Bob")
        self.assertEqual(worker.unit_type, "Worker")
        self.assertEqual(worker.strength, 1)
        self.assertEqual(worker.defense, 0)
        self.assertEqual(worker.hp, 5)
        self.assertEqual(worker.total_hp, 5)

    def test_archer_attack(self):
        archer = Archer("Robin")
        infantry = Infantry("Leonidas")
        initial_hp = infantry.hp
        damage = archer.attack(infantry)
        self.assertTrue(damage > 0)
        self.assertEqual(infantry.hp, initial_hp - damage)
        self.assertEqual(archer.arrows, 4)

    def test_cavalry_attack(self):
        cavalry = Cavalry("Maximus")
        archer = Archer("Robin")
        initial_hp = archer.hp
        damage = cavalry.attack(archer)
        self.assertTrue(damage > 0)
        self.assertEqual(archer.hp, initial_hp - damage)

    def test_infantry_attack(self):
        infantry = Infantry("Leonidas")
        cavalry = Cavalry("Maximus")
        initial_hp = cavalry.hp
        damage = infantry.attack(cavalry)
        self.assertTrue(damage > 0)
        self.assertEqual(cavalry.hp, initial_hp - damage)

    def test_worker_collect(self):
        worker = Worker("Bob")
        resources = worker.collect()
        self.assertEqual(resources, 10)

    def test_is_debilitated(self):
        archer = Archer("Robin")
        archer.hp = 0
        self.assertTrue(archer.is_debilitated())
        infantry = Infantry("Leonidas")
        infantry.hp = 5
        self.assertFalse(infantry.is_debilitated())

if __name__ == '__main__':
    unittest.main()