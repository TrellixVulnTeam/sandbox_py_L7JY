"""
Basic pytest demo
"""
import pytest

from phonebook import Phonebook


@pytest.fixture
def phonebook_with_clear():
    """Provides an empty Phonebook"""
    phonebook = Phonebook()
    yield phonebook
    phonebook.clear()


@pytest.fixture
def phonebook(tmpdir):
    """Provides an empty Phonebook with built-in tempdir"""
    return Phonebook(tmpdir)


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
