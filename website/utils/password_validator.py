'''
	    a password must have:
		+ at least 8 chars and max 15
		+ at least 1 numbers
		+ at least 1 of this --> '/.,@*$#_-&%'
		+ at least 1 of lowercase and uppercase letters
'''

# PARAMETERS
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
NUMBERS = list('1234567890')
SPECIAL_CHARS = list('/.,@*$#_-&%')
MIN_LEN = 8


def check_caps(password):
    ''' check the password for uppercase letters '''
    password = list(password)

    cap_count = 0

    for i in LETTERS:
        if i.upper() in password:
            cap_count += 1
    return cap_count


def special_chars(password):
    ''' check the password for special characters '/.,@*$#_-&%' '''
    password = list(password)

    sp_chars_count = 0

    for i in password:
        if i in SPECIAL_CHARS:
            sp_chars_count += 1
    return sp_chars_count


def check_int(password):
    ''' check the password for numbers '''
    password = list(password)

    int_count = 0

    for i in password:
        if i in NUMBERS:
            int_count += 1

    return int_count


def create_pw():
    ''' if the user password is weak suggest random generated password'''
    import random

    CAPS_LETTERS = [i.upper() for i in LETTERS]
    parameters = LETTERS + NUMBERS + SPECIAL_CHARS + CAPS_LETTERS

    # suggest password
    sugg_password = ''

    # generate random password
    for i in range(15):
        sugg_password += random.choice(parameters)

    return sugg_password


def validate(password):
    ''' checks if the password meets the the required standard'''
    caps_count = check_caps(password)
    int_count = check_int(password)
    sp_count = special_chars(password)

    # check if for minimum and maximum length
    if len(password) >= MIN_LEN:
        if all([caps_count, int_count, sp_count]):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    password = input('Enter password for validation: ')

    if validate(password):
        print('True')
    else:
        # if not valid password
        # generate password
        sugg_password = create_pw()
        good_pw = validate(sugg_password)
        while not good_pw:
            sugg_password = create_pw()
            good_pw = validate(sugg_password)

        print('Suggested password: ', sugg_password)
