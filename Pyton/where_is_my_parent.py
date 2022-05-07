def find_children(dancing_brigade):
    s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    return ''.join(sorted(dancing_brigade, key = s.index))