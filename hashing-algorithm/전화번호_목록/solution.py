# phone_book = ["88", "1235", "567","124", "12"]

def solution(phone_book):
    phone_book = sorted(phone_book)                 # ['12', '1235', '124', '567', '88']
    for idx, phone in enumerate(phone_book[:-1]):
        len_p = len(phone)
        if len_p > len(phone_book[idx+1]):
            continue
        if phone == phone_book[idx+1][:len_p]:
            return False
    return True
