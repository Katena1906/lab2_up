import unittest
import os
import requests
from main import find_credit_card_numbers, find_in_file, find_in_input_text, find_in_site

class TestFindCreditCardNumbers(unittest.TestCase):

    def test_find_credit_card_numbers(self):
        text = "Here are some card numbers: 1234-5678-9876-5432, 1111 2222 3333 4444, and invalid ones: 1234 5678 123."
        expected = ['1234-5678-9876-5432', '1111 2222 3333 4444']
        self.assertEqual(find_credit_card_numbers(text), expected)

    def test_find_no_credit_card_numbers(self):
        text = "My ID in Genshin 71-72-73-714"
        expected = []
        self.assertEqual(find_credit_card_numbers(text), expected)

    def test_find_multiple_formats(self):
        text = "Card numbers: 1234567898765432, 1234-5678-1234-5678, 1111 2222 3333 4444."
        expected = ['1234567898765432', '1234-5678-1234-5678', '1111 2222 3333 4444']
        self.assertEqual(find_credit_card_numbers(text), expected)

class TestFindInFile(unittest.TestCase):
    def test_find_in_file_valid(self):
        temp = "test.txt"
        with open(temp, "w", encoding="utf-8") as f:
            f.write("1222 5585 8585 9494\n4747 4884 4844 3373")
        expected =['1222 5585 8585 9494','4747 4884 4844 3373']
        self.assertEqual(find_in_file(temp), expected)
        os.remove(temp)

    def test_find_in_file_not_found(self):
        self.assertEqual(find_in_file("non_existent_file.txt"), [])

    def test_find_in_file_invalid_input(self):
        with self.assertRaises(TypeError):
            find_in_file(12345)




