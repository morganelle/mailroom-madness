"""Mailroom Madness module lets a user track and thank donors and donations."""


DONORS = {  # pragma no cover
    'ANNA SHELBY': [300],
    'MORGAN NOMURA': [10],
    'EDGAR POE': [1000]
}


def main():
    """Main function."""
    user_prompt()
    print('MAILROOM MADNESS!!')


def user_prompt():
    """Function that prompts user to choose to write a thank you or build a report."""
    print('Type Q to quit the program anytime')
    print('Would you like to write a thank you email to a donor or see a report of past donations?')
    choice = input('Type T for thank you or R for report: ').upper()
    options = ['T', 'R', 'Q']
    while choice not in options:
        print('Sorry, there is no option for what you typed.')
        choice = input('Please type T for thank you or R for report, or Q to quit: ').upper()
    if choice == 'R':
        print('--------------------------------------------')
        print('You chose report!!!')
    elif choice == 'T':
        thank_you_email()
    else:
        print('Thank you for looking at our program!')
        exit()


def thank_you_email():
    """Function that creates the thank you email for the user."""
    print('''
--------------------------------------------
You chose THANK YOU EMAIL!!
'Type B to return to main options
        ''')
    user_input = validate_user_name_input()
    if user_input == 'L':
        print(show_list(DONORS))
        # user_input = validate_user_name_input()
    elif user_input == 'B':
        user_prompt()
    else:
        build_email()


def validate_user_name_input():
    """Function that checks user inputs valid name or option."""
    user_input_valid = False
    options = ['B', 'L']
    while not user_input_valid:
        user_input = input('Enter First Name and Last Name for donor or type L to see a list of donors: ').upper().strip()
        if len(user_input.split(' ')) == 2 or user_input in options:
            user_input_valid = True
            print('user input:', user_input)
            return user_input


def show_list(donor_list):
    """Convert donor key name to list."""
    return list(donor_list.keys())


def build_email():
    """Function to build a thank-you email."""
    print('''
--------------------------------------------
WE ARE BUILDING AN EMAIL!
''')


if __name__ == '__main__':  # pragma no cover
    main()
