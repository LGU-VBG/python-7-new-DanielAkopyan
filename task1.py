spisok1=["da","osel","loshad"]
spisok2=[424,564,767]

def merge_lists_to_dict(a=spisok1,b=spisok2):
    s=zip(a,b)
    ok=dict(s)
    return ok


print(merge_lists_to_dict())
print(merge_lists_to_dict(["asdas"],b=[444]))