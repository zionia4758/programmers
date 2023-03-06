def solution(phone_book):
    phone_book.sort()
    book_len = len(phone_book)
    book_hash = {-1:False}
    for phone in phone_book:
        book = book_hash
        for p in phone:
            if p not in book:
                if book[-1]==True:
                    return False
                book[p]={-1:False}

            book = book[p]
        book[-1]=True
    return True
