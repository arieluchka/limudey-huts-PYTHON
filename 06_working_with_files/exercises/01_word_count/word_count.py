# write a function that receives a file and returns how many times each word shows
from jinja2.filters import do_default


# some_dict = {"is": 1}
#
# word = "are"
#
# some_dict[word] = 1
#
# word = "hello"
#
# some_dict[word] = 1
#
# some_dict[word] = some_dict[word] + 1
#
# print(some_dict)



# word = "hello world. how are you? my world is great."

# word_list = word.split(" ")

# w = "111222233333222222111111"
# print(w.strip("21"))



# for w in word_list:
#     print(w.strip("."))


# list1 = [1, 2 ,3]
# list2 = [4, 5, 6]
#
# list1.extend(list2)
# print(list1)



def count_all_word_types(desired_file: str):
    # 1) get all words
    #   a) read the whole file
    #   b) split all words into a list


    f = open(desired_file, mode="r")
    # whole_file = f.read()
    # word_list = whole_file.split(" ")
    # print(word_list)

    word_list = []

    for line in f.readlines():
        word_list.extend(line.split(" "))

    clean_word_list = []

    for word in word_list:
        if word == "\n":
            continue
        clean_word_list.append(word.strip("\n.,").lower())

    # print(clean_word_list)

    word_dict = {}

    for word in clean_word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict













all_word = count_all_word_types(desired_file="customs_day.txt")
# all_word = count_all_word_types(desired_file=".\\word_count.py")

print(all_word)