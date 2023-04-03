# This program takes in a Sum of Products equation, simplified or not, and given the variable names
# it creates the VHDL Code necessary to implement this equation
input_equation = input("Please enter the equation (Z=Y1*Y2'+Y1'*Y2): ") # Gets the overall equation
answer_side, equation_side = input_equation.split("=") # Splits it into output and input
min_terms = equation_side.split("+") # Gets each minterm separately
list_vhdl = []
for min_term in min_terms: # Iterates through each minterm
    min_term_split = min_term.split("*") #Separates each minterm into just the raw variables
    term_list = []
    for var in min_term_split: # Iterates through the variables
        if var[-1] == "\'": # Checks to see if this variale is negated
            term_list.append("(not " + var[:-1] + ")") # Turns negated variable into proper VHDL code
        else:
            term_list.append("(" + var + ")") # Turns normal variable into proper VHDL code
    vhdl_term = ""
    for term in term_list: # Converts each minterm into proper VHDL code
        vhdl_term += term + " and " 
    vhdl_term = vhdl_term[:-5] # Get's rid of extra 'and' that would be assigned to it
    list_vhdl.append("(" + vhdl_term + ")") # Use paranthesis to make VHDL code more precise
vhdl_equation = answer_side + " <= (" # Start off final VHDL equation with output and assignment operator
for vhdl_term in list_vhdl:
    vhdl_equation += vhdl_term + " or " # Joins minterms into Sum of Products in proper VHDL code
vhdl_equation = vhdl_equation[:-4] + ")" # Removes extra 'or' at the end of the equation
print(vhdl_equation) #Prints to console final output