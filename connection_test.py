import unittest
from unittest.mock import MagicMock
from connection import AccountManager

class TestAccountManager(unittest.TestCase):

    def setUp(self):
        # Mocking pyodbc connection and cursor
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor

        # Creating an instance of AccountManager with mocked connection
        self.account_manager = AccountManager(server="DESKTOP-K8BIO91\SQLEXPRESS", database="BankSystem")
        self.account_manager.connection = self.mock_connection



if __name__ == '__main__':
    unittest.main()
