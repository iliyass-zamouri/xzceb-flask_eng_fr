import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):

    def test_english_to_french_translation(self):
        english_text = 'Hello'
        french_text = englishToFrench(english_text)
        self.assertIsNotNone(french_text)

    def test_french_to_english_translation(self):
        french_text = 'Bonjour'
        english_text = frenchToEnglish(french_text)
        self.assertIsNotNone(english_text)

if __name__ == '__main__':
    unittest.main()
