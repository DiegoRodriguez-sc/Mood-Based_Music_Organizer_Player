import unittest
import os
import shutil
from file_operations import scan_music_directory, get_song_metadata, move_song_to_mood_folder, organize_music_by_mood

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_music'
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, 'test.mp3'), 'w') as f:
            f.write('dummy data')
        with open(os.path.join(self.test_dir, 'test2.mp3'), 'w') as f:
            f.write('dummy data')

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_scan_music_directory(self):
        files = scan_music_directory(self.test_dir)
        self.assertEqual(len(files), 2)

    def test_get_song_metadata(self):
        file_path = os.path.join(self.test_dir, 'test.mp3')
        metadata = get_song_metadata(file_path)
        self.assertIsInstance(metadata, dict)

    def test_move_song_to_mood_folder(self):
        file_path = os.path.join(self.test_dir, 'test.mp3')
        move_song_to_mood_folder(file_path, 'happy')
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'happy', 'test.mp3')))

    def test_organize_music_by_mood(self):
        def mock_categorize_by_mood(metadata):
            return 'happy'
        organize_music_by_mood(self.test_dir, mock_categorize_by_mood)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'happy', 'test.mp3')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'happy', 'test2.mp3')))

if __name__ == '__main__':
    unittest.main()
