#!/usr/bin/python3
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number = str(input("Enter Phone number: "))
number = f"+91{number}"
in_num=phonenumbers.parse(number,"CH")
# code = geocoder.description_for_number(in_num,lang="en")
country = geocoder.description_for_valid_number(in_num,lang="en")
print(country)
service_provider = carrier.name_for_number(in_num,lang="en")
# service_provider = carrier.name_for_valid_number(in_num,lang="en")
print(service_provider)

time = timezone.time_zones_for_number(in_num)
# time = timezone.time_zones_for_geographical_number(in_num)
print(time)

valid = phonenumbers.is_valid_number(phonenumbers.parse("+919818183950"))
print(valid)
