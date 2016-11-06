"""
Solution of Phonelist test code: of https://cmind.kattis.com/problems/phonelist
__author__ = "Carlos Eduardo Smaniotto"
__email__ = "csmanioto@gmail.com"
__date__ = "2016-11-06"
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""
method: check_quantity_test
This one check is the quantify of tests is valid...
return: True in case valid or false
"""
def check_quantity_test(numbers_test):
    check = False
    if 1 <= numbers_test <= 40:
        check = True
    return check


"""
method: check_input_quantity_phone
This one check is the quantify of the phone number per test is ok...
return: True in case valid or false
"""
def check_input_quantity_phone(n_input):
    check = False
    if 1 <= n_input <= 10000:
        check = True
    return check


"""
method: check_is_phone_number
This one check if the number is a valid phone number...
return: True in case valid or false
"""
def check_is_phone_number(phone_number):
    check = False
    if 1 <= len(phone_number) <= 10:
        check = True
    return check


"""
method: check_is_consistence
This one check the consistence of phone list.
return: True in case valid or false
"""
def check_is_consistence(phone_list):
    consistence = True
    phone_list.sort(key=len, reverse=False)
    for n1 in phone_list:
        for n2 in phone_list:
            if len(n1) < len(n2) and int(n2[:len(n1)]) == int(n1):
                logger.debug("Conflict between numbers {} and {}".format(n1, n2))
                consistence = False
                break
    return consistence


"""
method: from_console
This method get information to test from console:
inputs: quantity of tests; size of phone list and phone number of this list.
return: The Consistence status of each test.
"""
def from_console():
    number_test = int(input("Gives me the number(s) of test: \n"))
    # noinspection PyBroadException
    try:
        if check_quantity_test(number_test):
            for n_tests in range(start=1, stop=number_test + 1):
                logger.debug("Executing test {}".format(n_tests))
                phone_input = int(input("Numbers of phone-number you will input ? \n"))

                if check_input_quantity_phone(phone_input):
                    phone_list = list()
                    consistence = "NO"
                    for n_numbers in range(start=1, stop=phone_input + 1):
                        logger.debug("Will be inputted {} phone numbers".format(n_numbers))
                        phone_number = input("Enter the phone number to the list: \n")

                        if check_is_phone_number(phone_number):
                            phone_list.append(phone_number)
                    if check_is_consistence(phone_list):
                        consistence = "YES"
                    print("Test {} Consistence: {}".format(n_tests + 1, consistence))
    except:
        print("Houston we have a problem")


"""
method: from_file
This method read the file with based on sample.
input: file to test.
return: The Consistence status of each test.
"""
def from_file(filename):
    with open(filename, 'r') as phone_file:
        numbers_test = int(phone_file.readline().strip())
        if not check_quantity_test(numbers_test):
            logger.info("Impossible to continue...")
            exit(1)
        for n_testes in range(numbers_test):
            phone_input = int(phone_file.readline().strip())
            phone_list = list()
            consistence = "NO"
            for n_numbers in range(phone_input):
                phone_number = phone_file.readline().strip()
                logger.debug("Get phone numbers".format(phone_number))
                if check_is_phone_number(phone_number):
                    logger.debug("Test {} - phone number {}".format(n_testes, phone_number))
                    phone_list.append(phone_number)

            if check_is_consistence(phone_list):
                consistence = "YES"
            print("Test {} Consistence: {}".format(n_testes + 1, consistence))


if __name__ == "__main__":
    test_origin = input("You will input from Keyboard or File ? Please KB or filename: \n")
    if test_origin.lower().strip() == "kb":
        from_console()
    else:
        from_file(str(test_origin).strip())
