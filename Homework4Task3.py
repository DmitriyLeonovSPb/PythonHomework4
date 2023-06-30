# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение 
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def keys_to_dictionary(**arg_keys):
    answer = dict()
    for i, j in arg_keys.items():
        if isinstance(j, (list, dict, set, bytearray)):
            j = str(j)
        answer[j] = i
    return answer
print(keys_to_dictionary(director='Oleg', worker={'Ivan': 1, 'Vasiliy': 2}, manager=['Nikita', 'Anton'],
                     accountant={'Maria'}))