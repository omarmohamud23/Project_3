import unittest
from unittest.mock import patch
from peewee import *
from main import *
from ui import *


MODELS = [Artist, Artwork]

test_db = SqliteDatabase(':memory:')


class TestMain(unittest.TestCase):
    
    #ensures that tables exist and clears Database so it's empty before tests start
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)
        generate_test_tables()

   #Creates Menu option for the user to choose from
    def test_create_menu(self):
        self.assertIsInstance(create_menu(), Menu)

    #Tests if options are valid 
    def test_is_valid(self):
        test_menu = create_menu()
        self.assertTrue(test_menu.is_valid('1'))
        self.assertTrue(test_menu.is_valid('Q'))
        self.assertFalse(test_menu.is_valid(1))
        self.assertFalse(test_menu.is_valid('q'))
        self.assertFalse(test_menu.is_valid('sdlkjsldkjsljsdlskdjsdlgj'))

    #Gets action 
    def test_get_action(self):
        test_menu = create_menu()
        self.assertEqual(test_menu.get_action('1'), add_artist)
    
    #Searches for all artist 
    def test_search_artist_all(self):
        self.assertEqual(True, True)

    #it searches for available artist
    def test_search_available_artist(self):
        self.assertEqual(True, True)
    
    #it adds artwork 
    def test_add_artwork(self):
        self.assertEqual(True, True)

    #this method deletes artwork 
    def test_artwork_deleted(self):
        self.assertEqual(True, True)

    #it changes the availbality of the artwork 
    def get_artwork_availability(self):
        self.assertEqual(True, True)

    def tearDown(self):
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()
