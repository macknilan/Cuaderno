import random


def authorize_sms() -> bool:
    sms_code = str(random.randint(1000, 9999))
    print(f"Sent SMS code: {sms_code}")
    read_sms_code = input("Please enter the code sent to you by SMS: ")
    return read_sms_code == sms_code


def authorize_google() -> bool:
    auth_code = str(random.randint(100000, 999999))
    print(f"Google auth code: {auth_code}")
    read_auth_code = input("Please enter the Google auth code: ")
    return read_auth_code == auth_code


def authorize_robot() -> bool:
    read_auth_code = ""
    while read_auth_code != "y" and read_auth_code != "n":
        read_auth_code = input("Are you a robot (y/n)? ")
    return read_auth_code == "n"
