import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

# Enter phone number along with country code
number = input("Enter a phone number with country code (e.g., +91 8897909599): ")

# Parsing the string to a PhoneNumber object
phoneNumber = phonenumbers.parse(number)

# Getting the timezone for the phone number
timeZone = timezone.time_zones_for_number(phoneNumber)

# Getting the geolocation of the given number
geolocation = geocoder.description_for_number(phoneNumber, "en")

# Getting the service provider name for the phone number
service = carrier.name_for_number(phoneNumber, "en")

# Printing the results
print("Time Zone for the number is: " + str(timeZone))
print("Geo Location for the number is: " + geolocation)
print("Service Provider for the number is: " + service)
