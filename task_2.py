"""
 Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
 где ключ — значение переданного аргумента, а значение — имя аргумента. 
 Если ключ не хешируем, используйте его строковое представление.
"""

def keyword_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result


print(keyword_to_dict(a=1, b=2, c='three', d=[1, 2, 3], e={'key': 'value'}))