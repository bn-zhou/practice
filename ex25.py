

#将stuff按分隔符打断
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

#将单词排序
def sort_words(words):
    """Sort the words."""
    return sorted(words)

#从列表中删除一个元素（0是第一个，-1是最后一个）
def delet_first_word(words):
    """Delets the first word after popping it off."""
    word = words.pop(0)
    print (word)

#从列表中删除一个元素（0是第一个，-1是最后一个）
def delet_last_word(words):
    """Delets the last word after popping it off."""
    word = words.pop(-1)
    print = (word)

#将打断函数和排序函数整合为一个函数
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

#将打断函数和输出函数整合(列表未排序)
def delet_first_and_last(sentence):
    """Delets the first and last words of the sentence."""
    words = break_words(sentence)
    delet_first_word(words)
    delet_last_word(words)

#先将句子打断，再排序，再输出(列表已排序)
def delet_first_and_last_sorted(sentence):
    """Sorts the words then delets the first and last one."""
    words = sort_sentence(sentence)
    delet_first_word(words)
    delet_last_word(words)

#读取列表里的第一个单词
def read_fist_word(words):
    """Read the first word in the list."""
    print (words[0])

#读取列表里的最后一个单词
def read_last_word(words):
    """Read the last word in the list."""
    print (words[-1])


























