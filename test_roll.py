from roll import roll
import unittest
from unittest import mock   # pylint: disable=E0611

class TestRoll(unittest.TestCase):

    examples = [ 
        {'input': '5k2', 'in_bonus': 0, 'die_roll': 6, 'roll': 5, 'keep': 2, 'end_bonus':0, 'optimum_value': 12},
        {'input': '5k5', 'in_bonus': 0, 'die_roll': 5, 'roll': 5, 'keep': 5, 'end_bonus':0, 'optimum_value': 25},
        {'input': '4k5', 'in_bonus': 0, 'die_roll': 6, 'roll': 4, 'keep': 4, 'end_bonus':0, 'optimum_value': 24},
        {'input': '5k2', 'in_bonus': 5, 'die_roll': 6, 'roll': 5, 'keep': 2, 'end_bonus':5, 'optimum_value': 17},
        {'input': '5k2', 'in_bonus': -5, 'die_roll': 6, 'roll': 5, 'keep': 2, 'end_bonus':-5, 'optimum_value': 7},
        {'input': '12k5', 'in_bonus': 0, 'die_roll': 5, 'roll': 10, 'keep': 6, 'end_bonus':0, 'optimum_value': 30},
        {'input': '12k9', 'in_bonus': 0, 'die_roll': 5, 'roll': 10, 'keep': 10, 'end_bonus':0, 'optimum_value': 50},
        {'input': '11k10', 'in_bonus': 0, 'die_roll': 5, 'roll': 10, 'keep': 10, 'end_bonus':2, 'optimum_value': 52},
        {'input': '12k10', 'in_bonus': 0, 'die_roll': 5, 'roll': 10, 'keep': 10, 'end_bonus':4, 'optimum_value': 54},
        {'input': '15k9', 'in_bonus': 0, 'die_roll': 5, 'roll': 10, 'keep': 10, 'end_bonus':6, 'optimum_value': 56},
        {'input': '10k12', 'in_bonus': 0, 'die_roll': 5, 'roll': 10, 'keep': 10, 'end_bonus':4, 'optimum_value': 54},
        {'input': '14k12', 'in_bonus': 0, 'die_roll': 5, 'roll': 10, 'keep': 10, 'end_bonus':12, 'optimum_value': 62}
    ]

    def setUp(self):
        pass

    def test_help(self):
        with self.assertRaises(SystemExit) as cm:
            roll([])
        self.assertEqual(cm.exception.code, 0)
        with self.assertRaises(SystemExit) as cm:
            roll(['-h'])
        self.assertEqual(cm.exception.code, 0)
        with self.assertRaises(SystemExit) as cm:
            roll(['--help'])
        self.assertEqual(cm.exception.code, 0)

    @mock.patch('roll.randint')
    def test_working_mock(self, mock_randint):
        mock_randint.return_value = 6
        result = roll(['5k2'])
        self.assertTrue(mock_randint.called)
        self.assertTrue(result['optimum_value'], 12)

    @mock.patch('roll.randint')
    def test_examples(self, mock_randint):
        for expectation in self.examples:
            mock_randint.return_value = expectation['die_roll']
            result = roll([expectation['input'], expectation['in_bonus']])
            test_result(self, result, expectation)

    @mock.patch('roll.randint')
    def test_unskilled(self, mock_randint):
        mock_randint.return_value = 10
        result = roll(['5k2', '-u'])
        self.assertTrue(result['optimum_value'], 20)
        mock_randint.return_value = 10
        result = roll(['5k2', '--unskilled'])
        self.assertTrue(result['optimum_value'], 20)

    @mock.patch('roll.randint')
    def test_exploding(self, mock_randint):
        mock_randint.return_value = 9
        result = roll(['5k2', '-u', '-e', 9])
        self.assertTrue(result['optimum_value'], 18)
        mock_randint.return_value = 9
        result = roll(['5k2', '-u', '--explosion', 9])
        self.assertTrue(result['optimum_value'], 18)

def test_result(self, result, expectation):
    self.assertEqual( result['roll'],           expectation['roll'] )
    self.assertEqual( result['keep'],           expectation['keep'] )
    self.assertEqual( result['bonus'],          expectation['end_bonus'] )
    self.assertEqual( result['optimum_value'],  expectation['optimum_value'] )

if __name__ == '__main__':
    unittest.main()
