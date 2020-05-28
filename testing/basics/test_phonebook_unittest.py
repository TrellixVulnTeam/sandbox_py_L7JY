"""
Basic unittest demo
"""
import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phonebook = Phonebook()

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "1234")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("1234", number)

    def test_missing_name_raises_error(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())

    @unittest.skip('WIP')
    def test_phonebook_has_the_name_and_number(self):
        # transaction的なものについては、同時に複数のassertを行う
        self.phonebook.add("Sue", "123343")
        self.assertIn("Sue", self.phonebook.get_names())
        self.assertIn("123343", self.phonebook.get_numbers())
