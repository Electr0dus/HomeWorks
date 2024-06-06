def all_variants(text):
    for begin in range(len(text)):
        for end in range(begin + 1, len(text)+1):
            yield text[begin:end]



a = all_variants('abc')
for val in a:
    print(val)
