

#2-2 Simple messages (pg 19)
message = ('I told my friend,"Python is my favorite language"')
print(message)

#name.py (pg 20)
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#fullname.py (pg 21)
first_name = "ada"
last_name = "lovelace"
full_name = "{0} {1}".format(first_name,last_name)
print(full_name.title())
print("Hello, {0}".format(full_name.title()))
print(f"Hello, {full_name.title()}")

#addtab
tabbed_message = 'this is a tabbed message'
print(f"\t{tabbed_message}")

#newline
newline_message = ("     this is a\nnewline message")
print(newline_message.strip())

print(2 + 3*4)
print(3.0 ** 2)

#using underscores in numbers for readability
universe_age = 14_000_000_000
print("{:,}".format(universe_age))


#constants are all caps
MAX_CONNECTIONS = 5000
MAX_CONNECTIONS += 1
print(MAX_CONNECTIONS)
#the all caps is just best practice :( lol doesn't really make it a constant

import this
