import re
#Project1
#Part1
with open("original text.txt", "w+") as file:
    file.write("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'\n")
    file.write("J.U.U.U Kmltin.\n")
    file.write("mmps iks nmk eio; ---> hkmu\n")
    file.seek(0)
    read_lines = file.read()
def SwipeKeys(list1, list2):
    dict1 = {}
    for key1, key2 in zip(list1, list2):
        dict1[key1] = key2
        dict1[key2] = key1
    return dict1
#count the appearance of each letter
with open("original text.txt", "a+") as file:
    textt = "'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'\nJ.U.U.U kmltin.\nmmps iks nmk eio; ---> hkmu"
    def letter_counter(textt):
        textt = textt.lower()
        dict2 = {}
        for i in textt:
            if i.isalpha():
                dict2[i] = textt.count(i)
        return dict2
    print(letter_counter(textt))
#find the common letters in the original text file
def common_letter(textt):
    dict3 = {}
    for value in textt:
        if value.isalpha():
            value = value.lower()
            count = dict3.get(value, 0)
            count += 1
            dict3[value] = count
    result = dict(sorted(dict3.items(), key=lambda x: x[1], reverse=True)[:4])
    return SwipeKeys(list(result.keys()), ["e", "t", "o", "r"])
print(common_letter(read_lines))

#Part2
dictt = common_letter(textt)
def SwipeLetters(textt):
    text = read_lines
    for key in dictt:
        key = key.lower()
        text = text.replace(key, dictt[key])
new_text = "".join(dictt.get(letter, letter)for letter in textt)
print(new_text)

#Part3
def new_file(file_path):
    with open("original text.txt", "a+") as file:
        file.write(f"\nthe encryption for the text above is:\n{new_text}")
        file.seek(0)
    with open("results.txt", "w+") as file:
        file.write(new_text)
        file.seek(0)
new_file("C:/PycharmProjectsHWprojects/Project#1/Projectt1.py")

#Part4
#longest word function
def func1(longestWord):
    regex = re.compile('[^a-zA-Z]')
    _list = regex.sub(' ', new_text).split()
    print(_list)
    with open("results.txt", "r") as filedata:
        longestWordLength = len(max(_list, key=len))
        result = [textword for textword in _list if len(textword) == longestWordLength]
        return result
print(func1(new_text))
#nimber of lines function
def func2(lineNumber):
    with open("results.txt", "r") as filedata:
        length = len(filedata.readlines())
        return length
print(func2(new_text))
#main function
def main():
    with open("original text.txt", "a") as filedata:
        filedata.write("\n\n")
        filedata.write((func1(new_text)[0].upper() + " ")*func2(new_text))
        filedata.write("\n\n")
        for i in range(7):
            for j in range(7):
                if i == j or (6-j) == i:
                    filedata.write("*")
                else:
                    filedata.write(" ")
            filedata.write("\n")
if __name__ == "__main__":
    main()