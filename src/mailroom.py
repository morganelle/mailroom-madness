"""Mailroom Madness module lets a user track and thank donors and donations."""


DONORS = {  # pragma no cover
    'ANNA SHELBY': [300],
    'MORGAN NOMURA': [10],
    'EDGAR POE': [1000]
}

WELCOME = '''
\n
Welcome to Mailroom Madness!\n
Mailroom Madness is a state-of-the-art text-based interface
designed to help charitable organizations track, list, and
thank their donors.\n
Would you like to write a thank you email to a donor
or see a report of past donations?\n'''


MESSAGES = {
    'welcome': WELCOME,
    'email_or_report': 'Type T for thank you or R for report: ',
    'return_prompt': 'Type B to return to main options.',
    'quit': 'Type Q to quit Mailroom Madness.',
    'sorry_prompt': 'Sorry, there is no option for what you typed.',
    'sorry_input': 'Sorry, please enter a ',
    'get_donor': 'Enter First and Last Name for donor or type L to see a list of donors: ',
    'donation': 'number',
    'donor_name': 'First and Last Name',
    'input_donate': 'How much did {} donate? ',
    'goodbye': '\nThank you for using Mailroom Madness!\n',
    'border': '--------------------------------------------'
}


def main():
    """Main function."""
    print(MESSAGES['welcome'])
    user_prompt()
    final_choice()


def user_prompt():
    """Function that prompts user to choose to write a thank you or build a report."""
    print(MESSAGES['quit'])
    choice = validate_user_prompt()  # pragma no cover
    if choice == 'R':
        build_report()
    elif choice == 'T':
        thank_you_email()
    elif choice == 'Q':
        print(MESSAGES['goodbye'])


def validate_user_prompt():
    """Check user input for thank you or report."""
    options = ['T', 'R', 'Q']
    user_input = input(MESSAGES['email_or_report']).upper()  # pragma no cover
    while user_input not in options:
        print(MESSAGES['sorry_prompt'])
        user_input = input(MESSAGES['email_or_report']).upper()
    return user_input


def thank_you_email():
    """Function that creates the thank you email for the user."""
    print(MESSAGES['return_prompt'])
    user_input = validate_user_name_input()  # pragma no cover
    if user_input == 'L':
        print(show_list(DONORS))
        thank_you_email()
    elif user_input == 'B':
        user_prompt()
    else:
        add_donation(user_input, DONORS)
        build_email(user_input)


def validate_user_name_input():
    """Function that checks user inputs valid name or option."""
    user_input_valid = False
    options = ['B', 'L']
    user_input = input(MESSAGES['get_donor']).upper().strip()  # pragma no cover
    while not user_input_valid:
        if len(user_input.split(' ')) == 2 or user_input in options:
            user_input_valid = True
            print('user input:', user_input)
            return user_input
        else:
            print(MESSAGES['sorry_input'], MESSAGES['donor_name'], '.')


def show_list(donor_list):
    """Convert donor key name to list."""
    donor_lists = list(donor_list.keys())
    donor_lists.sort()
    return donor_lists


def add_donation(string_name, donor_list):
    """Add donation to donor."""
    find_donor(string_name, donor_list)
    donation_input = validate_donation_input(string_name) # pragma no cover
    donor_list[string_name].append(float(donation_input))
    print(donor_list)
    return donor_list[string_name]


def validate_donation_input(string_name):
    """Function that checks user inputs valid donation."""
    donation_input = input(MESSAGES['input_donate'].format(string_name))  # pragma no cover
    while not donation_input.isnumeric():
        print(MESSAGES['sorry_input'], MESSAGES['donation'], '.')
        donation_input = input('input_donate'.format(string_name))  # pragma no cover
    return donation_input


def find_donor(string_name, donor_list):
    """Create donor key in dictionary if it doesn't exist already."""
    if string_name not in donor_list:
        donor_list[string_name] = []
    return donor_list[string_name]


def build_email(user_input):
    """Build a thank-you email."""
    print(MESSAGES['border'])
    email = 'insert email here for {} with donation {}'.format(user_input, DONORS[user_input][-1])
    print(email)
    return email


def build_report():
    """Build a report showing donors sorted by donation."""
    print(MESSAGES['border'])
    print('<insert report here>')
    print(DONORS)


def final_choice():
    """Offer a choice to return to main options or exit."""
    user_input = input(MESSAGES['return_prompt'] + MESSAGES['quit']).upper()  # pragma no cover
    # validate user input
    if user_input == 'B':
        user_prompt()
    elif user_input == 'Q':
        print(MESSAGES['goodbye'])
        exit()


if __name__ == '__main__':  # pragma no cover
    main()
