# from fastapi import Body
from pydantic import BaseModel #, validator, ValidationError

class OTPVerificationResponse(BaseModel):
    """
    Response model for OTP verification
    """
    request_id: int
    mobile_number: str
    otp: str
    is_valid: bool

    # @validator("is_valid")
    # def validate_otp(cls, is_valid, values):
    #     """
    #     Validates the OTP with your chosen service
    #     """
    #     mobile_number = values.get("mobile_number")
    #     otp = values.get("otp")

    #     # Implement logic to call your OTP verification service
    #     # ...

    #     return is_valid

class OTPGenerationResponse(BaseModel):
    """
    Response model for OTP generation
    """
    request_id: int
    mobile_number: str
    otp: str
