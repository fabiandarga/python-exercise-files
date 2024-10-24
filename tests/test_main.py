import unittest
from src.main import read_csv_file


class TestFileReader(unittest.TestCase):
    def test_read_csv_file(self):
        result = read_csv_file("mitarbeiter.csv")

        # Prüfe, ob das Ergebnis eine Liste ist
        self.assertIsInstance(result, list)

        # Prüfe, ob die Liste nicht leer ist
        self.assertTrue(len(result) > 0)

        # Prüfe, ob das erste Element ein Dictionary ist
        self.assertIsInstance(result[0], dict)

        # Prüfe, ob alle erwarteten Schlüssel vorhanden sind
        expected_keys = {'name', 'age', 'role'}
        self.assertEqual(set(result[0].keys()), expected_keys)

        # Prüfe den ersten Datensatz
        self.assertEqual(result[0]['name'], 'Anna Schmidt')
        self.assertEqual(result[0]['age'], '34')
        self.assertEqual(result[0]['role'], 'Entwicklerin')


if __name__ == '__main__':
    unittest.main()
