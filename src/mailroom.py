"""Mailroom Madness module lets a user track and thank donors and donations."""


DONORS = {
    'Anna Shelby': [300],
    'Morgan Nomura': [10],
    'Edgar Allan Poe': [1000]
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
    if choice not in options:
        print('Sorry, there is no option for what you typed.')
        choice = input('Please type T for thank you or R for report, or Q to quit:')
    elif choice == 'R':
        print('You chose report!!')
    elif choice == 'T':
        print('You chose THANK YOU EMAIL!!')
    else:
        pass


if __name__ == '__main__':  # pragma no cover
    main()
