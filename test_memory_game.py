import unittest
from unittest.mock import Mock, patch
import sys
from memory_game import MemoryGame, TIME_LIMIT, PAIRS

sys.path.insert(0, '/c:/Users/Keerthana/Desktop/memory_puzzle_game_tkinter')

class TestRestartGame(unittest.TestCase):
    def setUp(self):
        self.root = Mock()
        self.game = MemoryGame(self.root)
    
    def test_restart_game_resets_time_left(self):
        self.game.time_left = 30
        self.game.restart_game()
        self.assertEqual(self.game.time_left, TIME_LIMIT)
    
    def test_restart_game_clears_flipped(self):
        self.game.flipped = [0, 1, 2]
        self.game.restart_game()
        self.assertEqual(self.game.flipped, [])
    
    def test_restart_game_clears_matched(self):
        self.game.matched = {0, 1, 2}
        self.game.restart_game()
        self.assertEqual(self.game.matched, set())
    
    @patch('memory_game.random.shuffle')
    def test_restart_game_shuffles_pairs(self, mock_shuffle):
        self.game.restart_game()
        mock_shuffle.assert_called_once()

if __name__ == '__main__':
    unittest.main()