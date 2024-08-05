import phonenumbers

def validate_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        print(parsed_number)
        if phonenumbers.is_valid_number(parsed_number):
            return True
        else:
            return False
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

# Example usage
phone_number = "9515997566"
if validate_phone_number(phone_number):
    print("Phone number is valid")
else:
    print("Phone number is invalid")