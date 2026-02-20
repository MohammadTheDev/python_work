from name_function import get_formatted_name


# def test_first_last_name():
#     """Does names like 'Janis Joplin' work?"""

#     first_name = "janis"
#     last_name = "joplin"

#     formatted_name = get_formatted_name(first_name, last_name)

#     assert formatted_name == "Janis Joplin"

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == "Wolfgang Amadeus Mozart"