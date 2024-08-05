from enum import Enum

class ErrorCode(Enum):
    """
    Enum class for error codes
    """
    TOO_MANY_FAILED_ATTEMPTS = (1, "Too many failed attempts error")
    SUCCESS = (0, "Success")
    INVALID_OTP = (2, "Invalid OTP error")
    INVALID_MOBILE_NUMBER = (3, "Invalid mobile number error")
    OTP_EXPIRED = (4, "OTP expired error")
    OTP_ALREADY_VERIFIED = (5, "OTP already verified error")
    OTP_NOT_FOUND = (6, "OTP not found error")
    OTP_GENERATION_FAILED = (7, "OTP generation failed error")
    OTP_VERIFICATION_FAILED = (8, "OTP verification failed error")
    OTP_SEND_FAILED = (9, "OTP send failed error")

    def __new__(cls, code, message):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.message = message
        return obj
