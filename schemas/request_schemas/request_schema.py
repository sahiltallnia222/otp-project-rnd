from fastapi import Body
from pydantic import BaseModel, validator, ValidationError
import phonenumbers

from ...configs import config

class OTPVerificationRequest(BaseModel):
    """
    VerificationRequest for otp 
    """
    mobile_number: str = Body(
        ..., description="Must be a valid mobile number."
    )
    otp: str = Body(..., regex=config.OTP_VALIDATION_STRING, description="Must be a 6-digit OTP.")

    extra: dict[str, str] = {}

    @validator("mobile_number")
    def validate_mobile_number(cls, mobile_number: str) -> str:
        """
        Validate the mobile number using phonenumbers library.
        """
        try:
            parsed_number = phonenumbers.parse(mobile_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError("Invalid mobile number.")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError("Invalid mobile number.")

        return mobile_number

class OTPGenerationRequest(BaseModel):
    """
    GenerationRequest for otp
    """
    mobile_number: str = Body(
        ..., description="Must be a 10-digit mobile number."
    )

    extra: dict[str, str] = {}

    @validator("mobile_number")
    def validate_mobile_number(cls, mobile_number: str) -> str:
        """
        Validate the mobile number using phonenumbers library.
        """
        print("Hi i am printing in validate_mobile_number in GenerationRequest Schema")
        try:
            parsed_number = phonenumbers.parse(mobile_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError("Invalid mobile number.")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError("Invalid mobile number.")

        return mobile_number
