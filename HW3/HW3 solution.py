#exercise1
info = {("Name"): "Roaya Heib", ("Age"): "19", ("PhoneNumber"): "0548344901"}
print(info)

#exercise2
def replaced_list(orig_list):
    try:
        orig_list[5] = '@'
    except IndexError:
        return "List too short"
    else:
        return orig_list
print(replaced_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(replaced_list([1, 2, 3, 4, 5]))

#exercise3
def replacedList(origList):
    try:
        assert len(origList) >= 6, "List too short"
        origList[5] = '@'
        return origList
    except AssertionError:
        return "List too short"
print(replacedList([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(replacedList([1, 2, 3, 4, 5]))

#exercise4
def UpDictionary(Dict1, inputKey, value):
    Dict1.update({inputKey: value})
    return Dict1
dictionary = {("Name"): "Roaya Heib", ("Age"): 19, ("PhoneNumber"): "0548344901"}
print(UpDictionary(dictionary, "Age", 19))
print(UpDictionary(dictionary, "I Live in", "Nazareth"))

#exercise5
n = 5
dictionary = {}
for i in range(1, n + 1):
    dictionary[i] = i + 3
print(dictionary)

#exercise6
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {}
for key in (dict1, dict2, dict3):
    dict4.update(key)
print(dict4)

#exercise7
def AppearCount(Stringgg):
    Stringgg = Stringgg.upper()
    dict1 = {}
    for Letter in Stringgg:
        count = dict1.get(Letter, 0)
        count += 1
        dict1[Letter] = count
    return dict1
print(AppearCount("ROAYA"))
print(AppearCount("RoAya"))

#exercise8
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {}
d1_keys = list(d1.keys())
d2_keys = list(d2.keys())
for key in d1_keys:
    if key in d2_keys:
        d3[key] = d1[key] + d2[key]
        d2_keys.remove(key)
    else:
        d3[key] = d1[key]
for key in d2_keys:
    d3[key] = d2[key]
print(d3)


