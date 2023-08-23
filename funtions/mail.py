email_address = input("Enter an email address: ")

def company_name(email):
    parts = email.split('@')
    if len(parts) == 2 and parts[1].endswith('.com'):
        name = parts[1][:-4]
        return name
    else:
        return None



name = company_name(email_address)
if company_name:
    print(name)
else:
    print("Invalid")
