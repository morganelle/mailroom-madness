# Pseudocode for Mailroom Madness
## Collaboration between Morgan Nomura and Anna Shelby

### data structure: 
- holding donors/donations amounts in key:value pairs
- Values should be a list.

### function: prompting user
    user alert: Type 'q' to quit the program at any time
    user input: choose between thank you, building a report, (q)
        if thank you, invoke sending a thank you
        if report, invoke building a report

### function: sending a thank you
    user alert: Type 'back' to get back to the original prompt
    user input: choose between full name, seeing a list, (q), (back)
        if full name, invoke identifying a name function
        if seeing a list
            invoke show
            re-prompt for name, (q), (back)
    invoke build email function

### function: show list
    show all names in the data structure

### function: identifying name
    look into data structure for name
    if the name is in the data structure, return it
    if the name isn't in the list, create it
    invoke function for adding a donation

### function: adding a donation:
    user input: enter donation amount, (q), (back)
    verify input is a number
    if input is not a number, reprompt, (q), (back)
    if input is a number, add to donor name

### function: build email:
    print formatted string with correct donor/donation amount

### function: creating a report
    sort list of donors by total donation amounts
    print formatted donor list, showing: Donor Name, total donated, number of donations and average donation amount as values
    user alert: Type 'back' to get back to the original prompt