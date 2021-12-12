def get_row_col(s):
    if s[0] not in ["A", "B", "C"] or not 0 <= int(s[1]) <=3:
        return "Error"
    else:
        return ((int(s[1])-1), ord(s[0]) - 65)

print(get_row_col("C3"))