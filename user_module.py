def read_file():
    with open("info_list.txt", "r") as file:
        # old is old_content and list type
        old = file.readlines()
    return old

def write_file(new):
    with open("info_list.txt", "w") as file:
        file.writelines(new)
        # you cannot use write() cus write argument should be string and writelines() aguments shld be sequence of string

