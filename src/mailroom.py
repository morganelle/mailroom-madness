"""Mailroom Madness module lets a user track and thank donors and donations."""


DONORS = {  # pragma no cover
    'ANNA SHELBY': [300, 10, 15],
    'MORGAN NOMURA': [10, 200, 50],
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
    'return_prompt': 'Type B to return to main options. ',
    'quit': 'Type Q to quit Mailroom Madness. ',
    'sorry_prompt': 'Sorry, there is no option for what you typed.',
    'sorry_input': 'Sorry, please enter a',
    'get_donor': 'Enter First and Last Name for donor or type L to see a list of donors: ',
    'donation': 'number',
    'donor_name': 'First and Last Name.',
    'input_donate': 'How much did {} donate? ',
    'goodbye': '\nThank you for using Mailroom Madness!\n',
    'border': '-' * 90
}


def main():
    """Main function."""
    print(MESSAGES['welcome'])
    user_prompt()


def user_prompt():
    """Function that prompts user to choose to write a thank you or build a report."""
    user_input = input(MESSAGES['email_or_report'] + MESSAGES['quit']).upper()  # pragma no cover
    user_input = validate_user_prompt(user_input, ['T', 'R', 'Q'], user_prompt)
    execute_user_choice(user_input)


def execute_user_choice(user_input):
    """Run function of valid user choice."""
    if user_input == 'Q':
        print(MESSAGES['goodbye'])
        exit()
        return 'quit'
    elif user_input == 'R':
        build_report()
        return 'report'
    elif user_input == 'T':
        thank_you_email()
        return 'thank you'
    elif user_input == 'B':
        user_prompt()
        return 'back'
    elif user_input == 'Q':
        print(MESSAGES['goodbye'])
        exit()
        return 'quit'
    else:
        return None


def validate_user_prompt(user_input, options, main_function):  # Tested
    """Check user input for thank you or report."""
    while user_input not in options:
        print(MESSAGES['sorry_prompt'])
        main_function()
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
            user_input = input(MESSAGES['get_donor']).upper().strip()  # pragma no cover


def show_list(donor_list):  # Tested
    """Convert donor key name to list."""
    donor_lists = list(donor_list.keys())
    donor_lists.sort()
    return donor_lists


def add_donation(string_name, donor_list):
    """Add donation to donor."""
    find_donor(string_name, donor_list)
    donation_input = validate_donation_input(string_name)  # pragma no cover
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


def find_donor(string_name, donor_list):  # Tested
    """Create donor key in dictionary if it doesn't exist already."""
    if string_name not in donor_list:
        donor_list[string_name] = []
    return donor_list[string_name]


def build_email(user_input):  # Tested
    """Build a thank-you email."""
    print(MESSAGES['border'])
    email = 'insert email here for {} with donation {}'.format(user_input, DONORS[user_input][-1])
    print(email)
    final_choice()
    return email


def build_report():
    """Build a report showing donors sorted by donation."""
    print(MESSAGES['border'])
    report = "{:<30}{:<20}{:<20}{:<20}{}{}{}".format("Donor Name", "Total Donations", "# of Donations", "Avg. Amount", "\n", MESSAGES["border"], "\n")
    for name in DONORS:
        report = report + "{:<30}{:<20}{:<20}{:<20.2f}{}".format(name, sum(DONORS[name]), len(DONORS[name]), sum(DONORS[name]) / len(DONORS[name]), "\n")
    print(report)
    final_choice()


def final_choice():
    """Offer a choice to return to main options or exit."""
    user_input = input(MESSAGES['return_prompt'] + MESSAGES['quit']).upper()  # pragma no cover
    user_input = validate_user_prompt(user_input, ['B', 'Q'], final_choice)
    execute_user_choice(user_input)


if __name__ == '__main__':  # pragma no cover
    main()
