from collections.abc import Iterable


def groupby(key, iterable: Iterable):
    result_dict = {}
    for elem in iterable:
        if elem[key] not in result_dict:
            result_dict[elem[key]] = list()
            result_dict[elem[key]].append(elem)
        else:
            result_dict[elem[key]].append(elem)
    return result_dict


users = [{'gender': 'female', 'age': 33}, {'gender': 'male', 'age': 20}, {'gender': 'female', 'age': 21}, ]
print(groupby('gender', users))
print(groupby('age', users))
