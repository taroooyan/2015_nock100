import re
import random
def replace_random(string):
    if len(string) > 4:
        population = range(1, len(string)-1)
        random_list = random.sample(population, len(string)-2)
        return_string = []
        return_string += string[0]
        for i in random_list:
            return_string += string[i]
        return_string += string[-1]
        return ''.join(return_string)
    else:
        return string
if __name__ == "__main__":
    # remove .,:
    pattern = re.compile('[,.:]')
    s = "I couldn't believe that I could actually understand \
            what I was reading : the phenomenal power of the human mind ."
    list_s = pattern.sub('', s).split()
    # print list_s
    for string in list_s:
        print replace_random(string)
