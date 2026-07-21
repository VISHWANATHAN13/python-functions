# variable keyword args function (kwargs)
# **kwargs collects keyword arguments into a dictionary.

def k_var_args(**kwargs):
    for key,value in kwargs.items():
        print(key," : ",value)

k_var_args(name="vishwa",age=22,course="B tech")