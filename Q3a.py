module_code = "CSC1009"

#Switch cases
switch = {
    "CSC1006": "Maths 2",
    "CSC1007": "Operating Systems",
    "CSC1008": "Data Structures and Algorithms",
    "CSC1009": "Object Oriented Programming",
    "CSC2902": "Communications In The Workplace"
}

#Prompts the user to input a  module code
module = input("Enter a module code: ")

#Prints the input the user entered and obtains the value from the switch case block
print(switch.get(module))

