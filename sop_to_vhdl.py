# os package is used to delete unused ".txt" files, allowing the program to declutter itself
import os
import time


def loading(t, increment=0.1, dots=3):
    t_end = time.time() + t
    while time.time() < t_end:
        print("\r               \r", end="")
        for i in range(dots):
            time.sleep(increment)
            print(". ", end="")
        time.sleep(increment)


def main():

    # Welcoming Message
    print(
        "\n"
        + "Welcome to the VHDL Code Converter! A tool that helps you implement basic VHDL components"
        + "\n"
        + "Using just the information provided, this program provides a VHDL implementation of you component."
        + "\n"
        + "\n"
        + "To start, sometimes working with this program can make this directory pretty messy because of the text files generated."
        + "\n"
    )

    # Gives user option to clean up directory
    del_files = input(
        'If you would like to delete some files that end with .txt in this directory, type "Y", if not, hit "enter"'
        + "\n"
        + "Enter choice here: "
    )
    if del_files == "Y":
        files_list = []
        file_input = ""
        print("\nThese are the current files in this directory: \n")
        for file in os.listdir(os.getcwd()):
            print(file[:-4])
        print(
            'One by one, please enter the headers of the .txt of the files you would like to save. Type ".." to not save anymore.'
        )
        while file_input != "..":
            file_input = input("Enter file name: ")
            files_list.append(f"{file_input}.txt")
        for item in os.listdir(os.getcwd()):
            if item.endswith(".txt") and (item not in files_list):
                os.remove(os.path.join(os.getcwd(), item))
        loading(2)
        print("\n\nFiles cleared!" + "\n" + "\n")

    # Gets the output file ready
    output_file_name = input(
        "What would you like the output file to be called (Do not include .txt): "
    )

    # Creates new output file, and writes to it. If "output_file_name.txt" already exists, it will overwrite it
    with open(output_file_name + ".txt", "w") as f:

        # Writes the header
        f.write("library ieee; use ieee.std_logic_1164.all;\n")

        # Starts creating the entity
        entity_name = input("What is your entity's name: ")
        f.write(f"entity {entity_name.upper()} is port(\n")

        # List that will later be provided to user so they know which inputs they can use
        input_names_list = []

        # Get's the inputs for the entity, formats it properly in VHDL
        print(
            f"Great, now I need some information about the inputs of \033[1m{entity_name}\033[0m."
        )
        num_of_types = int(input("How many different types of inputs do you have: "))
        input_list = []
        for i in range(num_of_types):
            input_type = ""
            typei = int(
                input(
                    f"Which of the following types is input group # {i+1}: "
                    + "\n"
                    + "0. std_logic"
                    + "\n"
                    + "1. std_logic_vector"
                    + "\n"
                    + "2. Other"
                    + "\n"
                    + "Enter choice here: "
                )
            )
            if typei == 1:
                size = int(input("What is the size of this std_logic_vector: "))
                input_type = f"std_logic_vector({size-1} downto 0)"
            elif typei == 0:
                input_type = "std_logic"
            elif typei == 2:
                input_type = input("Please input the type of variable you have: ")
            num_of_inputs = int(input("How many variables of this type do you have: "))
            input_names = []
            for j in range(num_of_inputs):
                input_name = input(f"What is the name of input # {j+1} of this type: ")
                input_names.append(input_name)
                input_names_list.append(input_name)
            input_list.append(
                f"     {', '.join(input_names)}:      in      {input_type}"
            )

        # List that will later be provided to user so they know which outputs they have to define
        output_names_list = []

        # Get's the outputs for the entity, formats it properly in VHDL
        print(f"Great, now I need some information about the outputs of {entity_name}.")
        num_of_types = int(input("How many different types of outputs do you have: "))
        output_list = []
        for i in range(num_of_types):
            output_type = ""
            typeo = int(
                input(
                    f"Which of the following types is output group # {i+1}: "
                    + "\n"
                    + "0. std_logic"
                    + "\n"
                    + "1. std_logic_vector"
                    + "\n"
                    + "2. Other"
                    + "\n"
                    + "Enter choice here: "
                )
            )
            if typeo == 1:
                size = int(input("What is the size of this std_logic_vector: "))
                output_type = f"std_logic_vector({size-1} downto 0)"
            elif typeo == 0:
                output_type = "std_logic"
            elif typeo == 2:
                output_type = input("Please input the type of variable you have: ")
            num_of_output = int(input("How many variables of this type do you have: "))
            output_names = []
            for j in range(num_of_output):
                output_name = input(
                    f"What is the name of output # {j+1} of this type: "
                )
                output_names.append(output_name)
                output_names_list.append(output_name)
            output_list.append(
                f"     {', '.join(output_names)}:      out      {output_type}"
            )

        # Write the VHDL formatted inputs and outputs to entity body, closes entity
        write_string = (";\n".join(input_list)) + ";\n" + (";\n".join(output_list))
        f.write(write_string + ");\n" + f"end {entity_name};\n\n")

        # Creates the header for architecture
        print("Great! The entity is created! Now time for the architecture!")
        arch_name = input(
            'What would you like to name the architecture (Usually "behavior" is default): '
        )
        f.write(f"architecture {arch_name} of {entity_name} is \n")

        # Checks if additional signals are necessary
        signals = bool(
            int(
                input(
                    "Are there any signals for the architecture you would like to define before you would like to proceed?"
                    + "\n"
                    + "0: No"
                    + "\n"
                    + "1: Yes"
                    + "\n"
                    + "Enter choice here: "
                )
            )
        )
        signals_list = []

        # If signals are necessary, formats their declaration and writes them to file below archietcure declaration
        if signals:
            num_signals = int(input("How many signals would you like to add: "))
            for i in range(num_signals):
                signal_name = input(f"What's the name of signal {i+1}: ")
                signals_list.append(signal_name)
                signal_type = input(f"What type is {signal_name}: ")
                f.write(f"signal {signal_name}: {signal_type};\n")

        # Begins the architecture body
        f.write("begin\n")

        # First will define signals in architecture body
        for signal in signals_list:
            value = input(f"What should signal {signal} be set to: ")
            f.write(f"{signal} <= {value};\n")

        # Get's ready for equation inputs
        print(
            "\n"
            + "Now it is time for the equations!"
            + "\n"
            + "Please enter the equations in this format:"
            + "\n"
            + "\n"
            + "\033[1m-- Z=Y(1)*Y(2)'+Y(1)'*Y(2) --\033[0m"
            + "\n"
            + "\n"
            + '- In this example, Z represents the output, Y1 and Y2 are inputs/signals. The " \' " represents the complement of that signal.'
            + "\n"
            + "- If you are inputting a node from a bus, you must use paranthesis to indicate which node it is (This is how VHDL does it)"
            + "\n"
            + '- If you wish to end inputting equations, type "END" and your session will be ended.'
            + "\n"
            + "- Please only use signals that you have declared earlier to prevent bugs in your VHDL code."
            + "\n"
            + "\n"
        )

        # Provides user with the inputs and outputs that they have already declared
        print(
            f"You have the following inputs: {', '.join(input_names_list)}"
            + "\n"
            + f"You have the following outputs: {', '.join(output_names_list)}"
            + "\n"
        )

        # Base variables
        input_equation = ""
        vhdl_equation = ""

        # Will continue until the user types "END"
        while input_equation != "END":

            # Gets the overall SOP equation, with output
            input_equation = input("Please enter the equation : ")

            # Ends loop if user requests
            if input_equation == "END":
                break

            # Splits the equation into output and inputs
            answer_side, equation_side = input_equation.split("=")

            # Strips any whitespace to prevent errors
            answer_side, equation_side = (
                answer_side.strip(),
                equation_side.strip(),
            )

            # Gets each minterm separately
            min_terms = equation_side.split("+")

            # Strips any whitespace to prevent errors
            min_terms = [min_term.strip() for min_term in min_terms]
            list_vhdl = []

            # Iterates through each minterm in the SOP equation
            for min_term in min_terms:

                # Separates each minterm into just the raw variables
                min_terms_split = min_term.split("*")

                # Strips any whitespace to prevent errors
                min_terms_split = [
                    min_term_split.strip() for min_term_split in min_terms_split
                ]
                term_list = []

                # Iterates through the variables in each midterm
                for var in min_terms_split:

                    # Gets proper VHDL code depending on if the variable is negated or not
                    if var[-1] == "'":
                        term_list.append("(not " + var[:-1] + ")")
                    else:
                        term_list.append("(" + var + ")")
                vhdl_term = ""

                # Combines the VHDL for each variable in the midterm so that the midterm is represented in proper VHDL code
                for term in term_list:
                    vhdl_term += term + " and "

                # Get's rid of extra 'and' that would be assigned to it
                vhdl_term = vhdl_term[:-5]

                # Use paranthesis to make VHDL code more precise
                list_vhdl.append("(" + vhdl_term + ")")

            # Start off final VHDL equation with output and assignment operator
            vhdl_equation = answer_side + " <= ("

            # Joins each minterm together with the "OR" operator, creating the SOP in VHDL code
            for vhdl_term in list_vhdl:
                vhdl_equation += vhdl_term + " or "

            # Removes extra 'or' at the end of the equation
            vhdl_equation = vhdl_equation[:-4] + ");"

            # Writes the equation to the text file
            f.write(f"      {vhdl_equation}\n")

        # Checks to see if there are any additional equations that aren't SOP that need to be added
        more_eq = bool(
            int(
                input(
                    "Are there any equations you would like to add that are not SOP?"
                    + "\n"
                    + "0. No\n"
                    + "1. Yes\n"
                    + "Enter choice here: "
                )
            )
        )

        # If there are, allows user to input these lines
        if more_eq:
            print(
                "Unfortunately, this tool cannot format any other types of equations for you, however you can manually input them."
                + "\n"
                + "Input them in the following format (This is a random example of a non-SOP equation):"
                + "\n"
                + "\n"
                + "Y <= B when (Sel = '1') else A;"
                + "\n"
            )
            ex_eq_cnt = input("How many more equations do you want to input: ")
            for i in range(ex_eq_cnt):
                equation = input("Please enter the equation: ")
                f.write(equation + "\n")

        # Ends the architecture body, thus finishing the entire VHDL code
        f.write(f"end {arch_name};")

    print(
        "\n"
        + f'All file have been written to \033[1m"{output_file_name}".\033[0m Good luck with your VHDL project!'
    )


if __name__ == "__main__":
    main()


# Future goals for this program:

#     - Have it generate the SOP equations itself
#     - Have it generate an entire digital component using VHDL just from a truth table and knowing which variables on that
#     truth table are inputs and outputs. The only information the program would be given is the csv file representing the
#     truth table, as long as there is some delimiter that separates the inputs and outputs.
#     - Not like it matters much, because the VHDL code being generated by this isn't complex enough to a point where
#     condensity matters, but implementing algorithms which determine the MSOP or MPOS equations from the truth table,
#     would allow for a more efficent and elegant solution.
