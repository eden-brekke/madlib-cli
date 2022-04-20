
def welcome():
    """
    print a welcome message for the user explaining the madlib processes
    """
    print('''
        Welcome to my first MadLib Game! 
        A Madlib is a pre-generated story for you to enter your own words into. 
        It's a fun way to pass the time.
    ''')


welcome()


def read_template(path):
    """
    read the text from the file given path
    where the path gets passed into the function call
    """
    try:
        with open(path, "r") as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(template):
    """
    Set some variables for the stripped variable,
    A list for the parts between the {}
    capture boolean for if we're in the process of capturing or not
    and the current part of each word which then gets pushed into the list.
    then we'll set the stripped to the characters in the for loop.
    then return the stripped  parts as a tuple to match the test
    """
    stripped = ""
    parts = []
    capture = False
    current_part = ""

    for character in template:
        if character == "{":
            stripped += character
            capture = True
            current_part = ""
        elif character == "}":
            stripped += character
            capture = False
            parts.append(current_part)
        elif capture:
            current_part += character
        else:
            stripped += character

    return stripped,tuple(parts)


def merge(template, tple):
    """
    take the template and format and break apart the tuple from the test.
    """
    return template.format(*tple)


