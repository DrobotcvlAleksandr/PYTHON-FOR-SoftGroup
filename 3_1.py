def is_palindrome(string):
    string = string.lower().replace(' ', '') # все в нижний регистр и удалим пробелы!
    rev_string = "".join(reversed(string)) # переворачиваем строку

    return string == rev_string #  сравниваем строку


print('True' if is_palindrome("Ee   v     ee") else 'Falls')