EXPECTED_BAKE_TIME = 40

def preparation_time_in_minutes(number_of_layers:int):
    return number_of_layers * 2 

def Bake_Time_Remaining(TimeINOven:int):
    return EXPECTED_BAKE_TIME - TimeINOven

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """

    return preparation_time_in_minutes(number_of_layers) + Bake_Time_Remaining(elapsed_bake_time)

print(elapsed_time_in_minutes.__doc__)
print(elapsed_time_in_minutes(3,20))