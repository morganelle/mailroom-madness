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
    choice = input('Type T for thank you or R for report: ').upper()  # pragma no cover
    options = ['T', 'R', 'Q']
    while choice not in options:
        print('Sorry, there is no option for what you typed.')
        choice = input('Please type T to write a thank-you email or R to see a report, or Q to quit: ').upper()
    if choice == 'R':
        print('--------------------------------------------')
        print('You chose report!!!')
    elif choice == 'T':
        print('''
--------------------------------------------
You chose THANK YOU EMAIL!!
        ''')
        thank_you_email()
    else:
        final_choice()


def thank_you_email():
    """Function that creates the thank you email for the user."""
    print('Type B to return to main options')
    user_input = validate_user_name_input()
    if user_input == 'L':
        print(show_list(DONORS))
        thank_you_email()
    elif user_input == 'B':
        user_prompt()
    else:
        add_donation(user_input, DONORS)
        build_email()


def validate_user_name_input():
    """Function that checks user inputs valid name or option."""
    user_input_valid = False
    options = ['B', 'L']
    user_input = input('Enter First and Last Name for donor or type L to see a list of donors: ').upper().strip()  # pragma no cover
    while not user_input_valid:
        if len(user_input.split(' ')) == 2 or user_input in options:
            user_input_valid = True
            print('user input:', user_input)
            return user_input
        else:
            print('Sorry, please enter a first and last name.')


def show_list(donor_list):
    """Convert donor key name to list."""
    donor_lists = list(donor_list.keys())
    donor_lists.sort()
    return donor_lists


def add_donation(string_name, donor_list):
    """Add donation to donor."""
    find_donor(string_name, donor_list)
    donation_input = validate_donation_input(string_name)
    donor_list[string_name].append(float(donation_input))
    print(donor_list)
    return donor_list


def validate_donation_input(string_name):
    """Function that checks user inputs valid donation."""
    donation_input = input('How much did {} donate? '.format(string_name))  # pragma no cover
    while not donation_input.isnumeric():
        print('Sorry, please enter a number.')
        donation_input = input('How much did {} donate? '.format(string_name))  # pragma no cover
    return donation_input


def find_donor(string_name, donor_list):
    """Create donor key in dictionary if it doesn't exist already."""
    if string_name not in donor_list:
        donor_list[string_name] = []
    return donor_list[string_name]


def build_email():
    """Build a thank-you email."""
    print('''
--------------------------------------------
INSERT EMAIL HERE
''')
    final_choice()


def build_report():
    """Build a report showing donors sorted by donation."""
    print('You chose report!!!')
    print(DONORS)
    final_choice()


def final_choice():
    """Offer a choice to return to main options or exit."""
    user_input = input('Type B to return to main options, or Q to exit: ').upper()
    # validate user input
    if user_input == 'B':
        user_prompt()
    elif user_input == 'Q':
        print('Thank you for using Mailroom Madness!')
        exit()


if __name__ == '__main__':  # pragma no cover
    main()
