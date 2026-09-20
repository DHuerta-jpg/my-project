def print_table(nested_list, column_names):
    num_cols = len(column_names)
    header_row = "| " + " | ".join(column_names) + " |"
    nice_horizontal_rule = ("|" + "-" * (len(header_row)-2)+"|")
    print(nice_horizontal_rule)
    print(header_row)
    print(nice_horizontal_rule)

    for item in nested_list:
        # writing each row to a string,
        # then printing the string, is better for performance:)
        s = "|"
        for i in range(num_cols):
            entry = str(item[i])
            s += (" "*(len(column_names[i]) - len(entry)+2) +
                entry + "|")
        print(s)
    print(nice_horizontal_rule)


my_nested_list = [
    ["Francis", "English", 435],
    ["Larry","Maths", 234],
    ["Nicole", "Biology", 986],
    ["Joey", "Physics", 562],
    ["Sam", "Computing", 12],
]

my_column_names = ["First Name", "Subject Chosen", "Score"]

print_table(my_nested_list, my_column_names)