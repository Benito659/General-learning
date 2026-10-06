def create_profile_1(**kwargs):
    return kwargs

def create_profile_2(**kwargs):
    return { key:value for key, value in kwargs.items()}
    
create_profile(name="Ben", age=30, country="Canada")