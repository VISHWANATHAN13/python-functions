# variable arguments function
# *args collects all positional arguments into a tuple.
def var_args(*args):
    for i in args:
        print(i)

var_args("one","two","three","four","five")