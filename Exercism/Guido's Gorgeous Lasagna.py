
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Coment"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(num_layer):
    """Coment"""
    return num_layer * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Coment"""
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time

print(bake_time_remaining.__doc__)
print(preparation_time_in_minutes.__doc__)
print(elapsed_time_in_minutes.__doc__)
