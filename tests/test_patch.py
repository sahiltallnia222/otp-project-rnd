import unittest
from unittest.mock import patch, Mock
from services.otp_service import OTPService

class MyFunctionTestCase(unittest.TestCase):

    @patch('services.otp_service')
    def test_my_function(self, mock_external_api_call):
        # Mock the external API call
        mock_external_api_call.return_value = 'Mocked response'

        # Call the function under test
        result = OTPService.generate_secret()

        # Assert the expected behavior
        self.assertEqual(result, 'Mocked response')
        mock_external_api_call.assert_called_once()

    def test_my_function_error(self):
        # Call the function under test without mocking the external API call
        with self.assertRaises(Exception):
            OTPService.generate_secret()

if __name__ == '__main__':
    unittest.main()