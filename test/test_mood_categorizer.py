import unittest
from mood_categorizer import categorize_by_mood

class TestMoodCategorizer(unittest.TestCase):

    def test_categorize_by_mood(self):
        mock_metadata = {'title': ['happy song'], 'artist': ['happy artist']}
        mood = categorize_by_mood(mock_metadata)
        self.assertEqual(mood, 'happy')

        mock_metadata = {'title': ['sad song'], 'artist': ['sad artist']}
        mood = categorize_by_mood(mock_metadata)
        self.assertEqual(mood, 'sad')

        mock_metadata = {'title': ['energetic song'], 'artist': ['energetic artist']}
        mood = categorize_by_mood(mock_metadata)
        self.assertEqual(mood, 'energetic')

        mock_metadata = {'title': ['calm song'], 'artist': ['calm artist']}
        mood = categorize_by_mood(mock_metadata)
        self.assertEqual(mood, 'calm')

        # Pruebas adicionales para asegurar la precisión
        mock_metadata = {'title': ['joyful tune'], 'artist': ['']}
        mood = categorize_by_mood(mock_metadata)
        self.assertEqual(mood, 'happy')

        mock_metadata = {'title': ['melancholic melody'], 'artist': ['']}
        mood = categorize_by_mood(mock_metadata)
        self.assertEqual(mood, 'sad')

if __name__ == '__main__':
    unittest.main()
