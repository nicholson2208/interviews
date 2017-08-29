def re_flatten(nested_list):
    temp_list = []
    for item in nested_list:
        if type(item) == list:
            item = re_flatten(item)
        temp_list.extend(item)
    return temp_list

if __name__ == "__main__":
    x = re_flatten([[[1,2],[3,4]],[5,6]])
    print x