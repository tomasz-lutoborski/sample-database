dictionary = {'one one': 1, 'two two': 2, 'three three': 3}

dict2 = dictionary

for key, value in dictionary.items():
    new_key = key.split()[0]
    dictionary[new_key] = dictionary.pop(key)

print(dictionary)
    
