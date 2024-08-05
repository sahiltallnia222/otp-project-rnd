import pyotp
import hashlib

class OTPService:
    def __init__(self):
        pass

    def generate_secret(self, mobile_number):
        """
        Generate secret key based on mobile number
        """
        secret = hashlib.sha256(mobile_number.encode()).hexdigest()
        return secret

    def generate_otp(self, secret):
        """
        Generate OTP
        """
        totp = pyotp.TOTP(secret)
        return totp.now()

    def verify_otp(self, secret, otp):
        """
        Verify OTP
        """
        totp = pyotp.TOTP(secret)
        return totp.verify(otp)

    def generate_otp_for_user(self, mobile_number):
        """
        Generate OTP for a user
        """
        secret = self.generate_secret(mobile_number)
        otp = self.generate_otp(secret)
        # Save the secret and OTP for the user, e.g., in a database
        # You can use the mobile_number as a unique identifier for the user
        return secret, otp
