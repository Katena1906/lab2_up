import unittest
from unittest.mock import patch, mock_open
import requests
from main import find_credit_card_numbers, find_in_file, find_in_input_text, find_in_site

class TestFindCreditCardNumbers(unittest.TestCase):

    def test_find_credit_card_numbers(self):
        text = "Here are some card numbers: 1234-5678-9876-5432, 1111 2222 3333 4444, and invalid ones: 1234 5678 123."
        expected = ['1234-5678-9876-5432', '1111 2222 3333 4444']
        self.assertEqual(find_credit_card_numbers(text), expected)

    def test_find_no_credit_card_numbers(self):
        text = "There are no card numbers here!"
        expected = []
        self.assertEqual(find_credit_card_numbers(text), expected)

    def test_find_multiple_formats(self):
        text = "Card numbers: 1234567898765432, 1234-5678-1234-5678, 1111 2222 3333 4444."
        expected = ['1234567898765432', '1234-5678-1234-5678', '1111 2222 3333 4444']
        self.assertEqual(find_credit_card_numbers(text), expected)
