import unittest
from models.user import User
from repositories.users_repository import save


class TestSaveUser(unittest.TestCase):
    def test_save_user(self):
        # Create a new user object
        user = User(name='John Doe', email='john.doe@example.com', phone='555-1234')

        # Save the user to the database
        saved_user = save(user)

        # Check that the saved user is not None
        self.assertIsNotNone(saved_user)

        # Check that the saved user's name, email, and phone are correct
        self.assertEqual(saved_user.name, 'John Doe')
        self.assertEqual(saved_user.email, 'john.doe@example.com')
        self.assertEqual(saved_user.phone, '555-1234')
