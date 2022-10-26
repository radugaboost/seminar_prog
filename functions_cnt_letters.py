def double_letter(string):
    s = set()
    for i in string:
        if string.lower().count(i) > 1 and i != ' ':
            s.add(i)
    return len(s)      

def count_duplicates(string):
    return len([ch for ch in (set(string.lower())) if string.lower().count(ch)>1])
