def say_hello(name):
    """
    Print the hello greeting to the console.

    :param name: The name of the person to say hello to
    :return: None
    """
    print("Hello " + name)


def default_argument_literal(initial_string, default="default value!"):
    """
    Print whatever the user inputs, plus a default value, unless it's overridden.

    :param initial_string: Initial string
    :param default: A default hard-coded string, which can be overridden
    :return: None
    """
    print(initial_string, default)


def variable_args_tuple_mapping(*args):
    """
    Print out a list of given positional arguments.

    :param args: A set of positional parameters, which will be mapped to a tuple within the function
    :return: None
    """
    for arg in args:
        print(arg)


def variable_args_dict_mapping(**args):
    """
    Print out the given keyword arguments.

    :param args: A set of keyword parameters, which will be mapped to a dictionary type within the function
    :return: None
    """
    for arg in args:
        print(arg, ":", args[arg])


if __name__ == "__main__":
    """
    Demonstrate how to call various functions.
    """
    say_hello("The Knights Who Say Ni")

    default_argument_literal("Oh look, a flying...")
    default_argument_literal("Oh look, a flying...", "circus!")

    variable_args_tuple_mapping("positional parameter 1", "positional parameter 2")

    variable_args_dict_mapping(starter="spam", main="more spam", dessert="spam flavoured ice-cream", drink="spam juice")
