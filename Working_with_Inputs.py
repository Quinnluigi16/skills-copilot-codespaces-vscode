# Each function named below respectfully validated each input for their respected field. 
# For the input_validation_emp_id function it validated for the length of the input and ensuiring that it is a 7 digit or less number. 
# The input_validation_emp_name function validates that the input is a string and doesn't contain special characters.
# THe input_validation_employ_email validates the input for a valid email while ensuring that it contains an @ in it.
# The input_validation_emp_address validates the input ensuring that the address only contains letter and no symbol.

def input_validation_emp_id(employ_id):
    if employ_id.isdigit() and len(employ_id) <= 7:
        return True
    return False
def input_validation_emp_name(employ_name):
    invalid_chars = set('!"\'#$%^&*()=+,<>/?;:[]{}\\')
    if employ_name.isalpha() or all(c.isalpha() or c.isspace() for c in employ_name):
        if not any(char in employ_name for char in invalid_chars):
            return True
    return False
def input_validation_employ_email(employ_email):
    # Allowed characters for email: alphanumeric, @, ., _, and -
    invalid_chars = set('!"\'#$%^&*()=+,<>/?;:[]{}\\')
    
    # Ensure the email contains only allowed characters
    if any(char in invalid_chars for char in employ_email):
        return False

    # Check if email has exactly one '@' and a valid domain with at least one '.'
    if employ_email.count('@') == 1:
        local_part, domain_part = employ_email.split('@')
        
        # Validate the local part (before @)
        if not local_part or not all(c.isalnum() or c in "._-" for c in local_part):
            return False
        
        # Validate the domain part (after @)
        if '.' in domain_part and domain_part[0] != '.' and domain_part[-1] != '.':
            if all(c.isalnum() or c in ".-" for c in domain_part):
                return True
    
    return False
def input_validation_emp_address(employ_address):
    invalid_chars = set('!"\'#$%^&*()=+,<>/?;:[]{}\\')
    if employ_address == "":
        return True
    if employ_address.isalnum() or all(c.isalnum() or c.isspace() for c in employ_address):
        if not any(char in employ_address for char in invalid_chars):
            return True
    return False

# I Created a function that will loop throguh the body and it'll break if any input returns a false value, while also printing out two potential strings depending on if an email was detected.
def main():
    employ_id = input("Please enter your employee ID: ")
    if not input_validation_emp_id(employ_id):
        print(f"The employee ID {employ_id} is invalid. Please try again.")
        return False
    employ_name = input("Please entor your name here: ")
    if not input_validation_emp_name(employ_name):
        print("Invalid Entry, Try again")
        return False
    employ_email = input("Whats your preffered email? ")
    if not input_validation_employ_email(employ_email):
        print("Invalid Email address, please try again shortly")
        return False
    employ_address = input("Whats your preffered address? ")
    if not input_validation_emp_address(employ_address):
        print("Invalid Email address, please try again shortly")
        return False
    
    if employ_address:
        print(f"Hi, {employ_name}, Your ID is {employ_id}, and your email is: {employ_email}. Finally your address is: {employ_address}")
    else:
        print(f"Hi, {employ_name}, Your ID is {employ_id}, and your email is: {employ_email}. No address was entered.")

if __name__== "__main__":
    main()
    
    

