import unittest
import requests
from main import find_credit_card_numbers, find_in_file, find_in_input_text, find_in_site
from unittest.mock import patch, Mock, mock_open

class TestFindCreditCardNumbers(unittest.TestCase):
    def test_find_credit_card_numbers(self):
        text = "Here are some card numbers: 1234-5678-9876-5432, 1111 2222 3333 4444, and invalid ones: 1234 5678 123."
        expected = ['1234-5678-9876-5432', '1111 2222 3333 4444']
        self.assertEqual(find_credit_card_numbers(text), expected)

    def test_find_no_credit_card_numbers(self):
        text = "My ID in Genshin 71-72-73-714, blatnoy yep?"
        expected = []
        self.assertEqual(find_credit_card_numbers(text), expected)

    def test_find_multiple_formats(self):
        text = "Card numbers: 1234567898765432, 1234-5678-1234-5678, 1111 2222 3333 4444."
        expected = ['1234567898765432', '1234-5678-1234-5678', '1111 2222 3333 4444']
        self.assertEqual(find_credit_card_numbers(text), expected)

class TestFindInFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="1222 5585 8585 9494\n4747 4884 4844 3373")
    def test_find_in_file_valid(self, mock_open):
        expected =['1222 5585 8585 9494','4747 4884 4844 3373']
        self.assertEqual(find_in_file("test.txt"), expected)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_find_in_file_not_found(self, mock_open):
        self.assertEqual(find_in_file("non_existent_file.txt"), [])

    def test_find_in_file_invalid_input(self):
        with self.assertRaises(TypeError):
            find_in_file(12345)


class TestFindInInputText(unittest.TestCase):
    @patch("builtins.input", return_value="My card is 4111 1111 1111 1111")
    def test_find_in_input_text_manual(self, mock_input):
        result = find_in_input_text()
        expected = ["4111 1111 1111 1111"]
        self.assertEqual(result, expected)


class TestFindInSite(unittest.TestCase):
    @patch("main.requests.get")
    @patch("main.find_credit_card_numbers", return_value=["4111 1111 1111 1111"])
    def test_find_in_site_valid(self, mock_find, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>My card is 4111 1111 1111 1111</body></html>"
        mock_get.return_value = mock_response
        result = find_in_site("http://example.com")
        mock_get.assert_called_once_with("http://example.com")
        mock_find.assert_called_once_with("My card is 4111 1111 1111 1111")
        self.assertEqual(result, ["4111 1111 1111 1111"])

    @patch("main.requests.get")
    def test_find_in_site_request_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")
        result = find_in_site("http://example.com")
        mock_get.assert_called_once_with("http://example.com")
        self.assertEqual(result, [])

    def test_find_in_site_invalid_input(self):
        with self.assertRaises(TypeError):
            find_in_site(12345)







