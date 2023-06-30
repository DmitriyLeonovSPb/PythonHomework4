def task_about_s(*words):
    words = list(words)
    temp = []
    lenghtt = len(words)
    for i in range(lenghtt):
        if words[i].endswith('s') and words[i] != 's':
            temp.append(words[i])
            words[i] = None
    for i in range(lenghtt):
        if words[i] is not None:
            words[i] += ''.join([i for i in temp])
    return words
print(task_about_s('s', 'smart', 'cosinus', 'tigers'))