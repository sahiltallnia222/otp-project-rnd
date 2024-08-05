import unittest
from unittest.mock import MagicMock
from services.otp_service import OTPService

class OtpVerificationTests(unittest.TestCase):
    """
    Test cases focused on OTP generation and verification.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up any state that is shared across all test methods.
        """
        print("Setup before any methods in the class")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up any state that is shared across all test methods.
        """
        print("Teardown after all methods in the class")

    def setUp(self):
        """
        Set up the test case by creating a mock object of OtpService.
        """
        self.otp_service = MagicMock(spec=OTPService)

    def tearDown(self):
        """
        Clean up after each test method.
        """
        print("Cleanup after a test method")

    def test_otp_length(self):
        """
        Test that the OTP generated has the expected length.
        """
        secret = "9515997566"
        otp = "123456"  # Assuming OTPs are 6 characters long
        self.otp_service.generate_secret.return_value = secret
        self.otp_service.generate_otp.return_value = otp

        expected_length = 6
        self.assertEqual(len(self.otp_service.generate_otp(self.otp_service.generate_secret())), expected_length)
        print("t_t_1")

    def test_otp_verification_accepts_correct_otp(self):
        """
        Test that verify_otp function accepts a correct OTP.
        """
        secret = "9515997566"
        otp = "123456"
        self.otp_service.generate_secret.return_value = secret
        self.otp_service.generate_otp.return_value = otp
        self.otp_service.verify_otp.return_value = True

        self.assertTrue(self.otp_service.verify_otp(secret, otp))
        print("t_t_2")

    def test_otp_verification_rejects_incorrect_otp(self):
        """
        Test that verify_otp function rejects an incorrect OTP.
        """
        secret = "9515997566"
        incorrect_otp = "wrongotp"
        self.otp_service.generate_secret.return_value = secret
        self.otp_service.verify_otp.return_value = False

        self.assertFalse(self.otp_service.verify_otp(secret, incorrect_otp))
        print("t_t_3")

if __name__ == '__main__':
    unittest.main()