

def math_operations(string):
    """ takes in the string when given a math equation and returns
    the answer. """

    return('i do math equations here')


def parser(string):
    """ Evaluates the string and returns whats needed."""

    return(string)


def run_lisp():
    """Main function 
    this will run the program continuosly"""

    while True:
        current_string = input('lisp-0122:')
        final_string = parser(current_string)

        print(final_string)



if __name__ == '__main__':
    run_lisp()