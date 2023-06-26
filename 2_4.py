# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return ''.join([symbol for symbol in s if symbol != "!"])
    # new_s = ''
    # for symbol in s: 
    #     if symbol != '!': new_s += symbol 
    # print(new_s)

print(remove_exclamation_marks("Oh, no!!!"))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    return (s[:-1] if s[len(s) - 1] == "!" else s)
    # new_s = ""
    # if s[len(s) - 1] == "!": new_s = s[:-1]
    # else: new_s = s
    # print(new_s) 
    

print(remove_last_em("!Hi"))


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    new_s = ''
    for word in s.split(" "): 
        quantity_symbol = 0
        for symbol in word: 
            if symbol == '!': quantity_symbol += 1
        if quantity_symbol != 1: new_s += word
    return new_s

print(remove_word_with_one_em("Hi! !Hi! Hi!"))