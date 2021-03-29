import re


def sorting(garbage: str) -> str:
    keys_upper, keys_lower = ['PL', 'GL', 'PA', 'MG'], ['pl', 'gl', 'pa', 'mg']
    green_peace = "plastic:{0}; glass:{1}; paper:{2}; mixed-garbage:{3};"
    love = lambda x, y: re.findall(r"{0}".format(x), garbage) + re.findall(r"{0}".format(y), garbage)
    temp_list = map(love, keys_upper, keys_lower)
    sorted_garbage = tuple((temp, len(temp)) for temp in temp_list)
    return green_peace.format(sorted_garbage[0], sorted_garbage[1], sorted_garbage[2], sorted_garbage[3])


print(sorting("PLglglMGmgplplpaPApaGL"))
