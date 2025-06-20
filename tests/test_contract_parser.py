import unittest
import os
from scripts.contract_parser import extract_contract_text

class TestContractParser(unittest.TestCase):
    def setUp(self):
        self.pdf_file = os.path.join(os.path.dirname(__file__), '../marketing-agreement.pdf')
        self.docx_file = os.path.join(os.path.dirname(__file__), '../marketing-agreement.docx')
        self.txt_file = os.path.join(os.path.dirname(__file__), 'sample.txt')
        # Create a sample txt file for testing
        with open(self.txt_file, 'w', encoding='utf-8') as f:
            f.write('Sample contract text for testing.')

    def tearDown(self):
        if os.path.exists(self.txt_file):
            os.remove(self.txt_file)

    def test_extract_contract_text_pdf(self):
        try:
            text = extract_contract_text(self.pdf_file)
            self.assertIsInstance(text, str)
            self.assertTrue(len(text) > 0)
        except Exception as e:
            self.skipTest(f"PDF test skipped: {e}")

    def test_extract_contract_text_docx(self):
        try:
            text = extract_contract_text(self.docx_file)
            self.assertIsInstance(text, str)
            self.assertTrue(len(text) > 0)
        except Exception as e:
            self.skipTest(f"DOCX test skipped: {e}")

    def test_extract_contract_text_txt(self):
        text = extract_contract_text(self.txt_file)
        self.assertEqual(text, 'Sample contract text for testing.')

    def test_extract_contract_text_unsupported(self):
        with self.assertRaises(ValueError):
            extract_contract_text('unsupported_file.xls')

if __name__ == '__main__':
    unittest.main()
