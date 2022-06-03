def format_name(f_name, l_name):
    return f_name + " " + l_name
f_name = input("\nEnter your first name: ").title()
l_name = input("\nEnter your last name: ").title()
print("\n" + format_name(f_name, l_name) + "\n")