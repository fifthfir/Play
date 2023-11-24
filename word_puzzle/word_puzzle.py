DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]


def search_word(sheet, word_lst):
    start = []
    end = []
    for y in range(len(sheet)):
        for x in range(len(sheet)):
            for dx, dy in DIRECTIONS:
                end = search_word_helper(sheet, x, y, dx, dy, word_lst)
                if end is not None:
                    start = [end[0] - (len(word_lst) - 1) * dx, end[1] - (len(word_lst) - 1) * dy]
                    return [start, end]


def search_word_helper(sheet, x, y, dx, dy, word_lst):
    if sheet[y][x] == word_lst[0]:
        if len(word_lst) == 1:
            return [x, y]
        else:
            x += dx
            y += dy
            if x >= 0 and x < len(sheet) and y >= 0 and y < len(sheet):
                return search_word_helper(sheet, x, y, dx, dy, word_lst[1:])
    return None


def make_sheet():
    sheet_len = int(input("Enter the length of the word puzzle:\n"))  # n * n
    sheet = []
    for i in range(sheet_len):
        sheet_i_str = input(f"Enter the {i+1}th line: ({sheet_len-1-i} lines left)\n")
        sheet_i_lst = [letter for letter in sheet_i_str]
        sheet.append(sheet_i_lst)

    print_sheet(sheet)

    return sheet


def print_sheet(sheet):
    sheet_len = len(sheet)
    print(f"Here is the sheet: ({sheet_len}*{sheet_len})")
    print("----------------------------------------")
    for i in range(sheet_len):
        print(sheet[i])
    print("----------------------------------------")


def modify_sheet(sheet):
    action = input("c to change sheet[x][y], d to delete sheet[x][y], a to add sheet[x][y]:\n")
    x = int(input("Enter x: \n"))
    y = int(input("Enter y: \n"))
    print(f"Sheet[{x}][{y}]: {sheet[x][y]}")

    if action == 'c':
        new = input("Change it into: \n")
        sheet[x][y] = new
    elif action == 'd':
        sheet[x].pop(y)
    elif action == 'a':
        add = input("Add a letter: \n")
        sheet[x].insert(y, add)

    print_sheet(sheet)

    return sheet


def main():
    sheet = make_sheet()
    while True:
        word = input("Enter a word: (l to leave, r to rewrite the sheet, c to modify the sheet)\n")
        if word == 's':
            break
        elif word == 'r':
            sheet = make_sheet()
        elif word == 'c':
            sheet = modify_sheet(sheet)
        else:
            word_lst = [letter for letter in word]
            result = search_word(sheet, word_lst)
            print(result)


main()
