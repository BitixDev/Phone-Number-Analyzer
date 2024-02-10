import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def analyze_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        region = geocoder.description_for_number(parsed_number, "en")
        operator = carrier.name_for_number(parsed_number, "en")
        country = phonenumbers.region_code_for_number(parsed_number)
        time_zone = timezone.time_zones_for_number(parsed_number)
        possible_formats = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        owner = "Unavailable"
        if phonenumbers.is_possible_number(parsed_number):
            owner = geocoder.description_for_number(parsed_number, "en")
        return {
            "region": region,
            "operator": operator,
            "country": country,
            "time_zone": time_zone,
            "possible_formats": possible_formats,
            "owner": owner
        }
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    phone_number = input("Enter the phone number in E.164 format (e.g., +1234567890): ")
    result = analyze_phone_number(phone_number)
    if "error" in result:
        print("Error:", result["error"])
    else:
        print("Region:", result["region"])
        print("Operator:", result["operator"])
        print("Country:", result["country"])
        print("Time Zone:", result["time_zone"])
        print("Possible Formats:", result["possible_formats"])
        print("Owner:", result["owner"])
