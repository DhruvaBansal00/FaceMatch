from random import randint

# ran_class = randint(0,3)
def get_class():
    ran_class = randint(0,3)

    if ran_class == 0:
        class_model = 0

    elif ran_class == 1:
        class_model = 3

    elif ran_class == 2:
        class_model = 4
        
    else:
        class_model = 6

    return class_model