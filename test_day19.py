from day19 import FusionPlant
import unittest

class TestFusionPlant(unittest.TestCase):
    TEST_REACTIONS = [
        ('H', 'HO'),
        ('H', 'OH'),
        ('O', 'HO')
    ]

    def test_create_fusion_plant(self):
        FusionPlant(self.TEST_REACTIONS)

    def test_generate_molecules(self):
        plant = FusionPlant(self.TEST_REACTIONS)
        self.assertEqual(len(plant.all_possible_molecules('HOH')), 4)
        self.assertEqual(len(plant.all_possible_molecules('HOHOHO')), 7)

if __name__ == '__main__':
    unittest.main()
