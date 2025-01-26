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

w = "111222233333222222111111"
print(w.strip("21"))



# for w in word_list:
#     print(w.strip("."))
#     print(w.split("")[0])




def count_all_word_types(desired_file: str):
    f = open(desired_file, mode="r")

    # 1) get all words
    #   a) read the whole file
    #   b) split all words into a list



    return # -> is = 5; are = 8  -> [["is", 5], ["are",8]]





all_word = count_all_word_types(desired_file=".\\customs_day.txt")
all_word = count_all_word_types(desired_file=".\\word_count.py")

print(all_word)