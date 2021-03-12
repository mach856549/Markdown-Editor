string_compile = []

def help(list_local):
    str1 = " "
    print(f"Available formatters: {str1.join(list_local)}")
    print("Special commands: !help !done")

def error():
    print("Unknown formatting type or command")


def done():
    my_file = open("output.md", "w")
    str3 = ""
    my_file.write(str3.join(string_compile))
    my_file.close()
    exit()


def valid_selection(selection):
    if selection == "plain":
        save_text(plain())
    elif selection == "bold":
        save_text(bold())
    elif selection == "italic":
        save_text(italic())
    elif selection == "link":
        save_text(link())
    elif selection == "inline-code":
        save_text(inline_code())
    elif selection == "header":
        save_text(header())
    elif selection == "line-break":
        save_text(line_break())
    elif selection == "ordered-list":
        save_text(list("1."))
    elif selection == "unordered-list":
        save_text(list("*"))
    else:
        print("Something went wrong")
        main_code()


def plain():
    user_text = input("Text: ")
    return user_text


def bold():
    user_text = input("Text: ")
    return "**" + user_text + "**"


def italic():
    user_text = input("Text: ")
    return "*" + user_text + "*"


def inline_code():
    user_text = input("Text: ")
    return "`" + user_text + "`"


def link():
    label = input("Label: ")
    url = input("URL: ")
    return "[" + label + "](" + url + ")"


def header():
    level = int(input("Level: "))
    if 1 <= level <= 6:
        user_text = input("Text: ")
        return "#" * level + " " + user_text + "\n"
    else:
        print("The level should be within the range of 1 to 6")
        return valid_selection("header")


def list(n):
    # n = "1." (ordered), n = "*" (unordered)
    rows = int(input("Number of rows: "))
    text_local = ""
    if rows > 0:
        for i in range(rows):
            start = "*" if n == "*" else str(i + 1) + "."
            user_text = input(f"Row #{i + 1}")
            text_local += start + " " + user_text + "\n"
        return text_local
    else:
        print("The number of rows should be greater than zero")
        return list(n)


def line_break():
    return "\n"


def save_text(text):
    global string_compile
    string_compile.append(text)
    str2 = ""
    print(str2.join(string_compile))


def main_code():
    valid_options = ["plain", "bold", "italic", "link", "inline-code", "header", "ordered-list", "unordered-list",
                     "line-break"]
    usr_select = input("- Choose a formatter:")
    if usr_select == "!help":
        help(valid_options)
    elif usr_select == "!done":
        done()
    elif usr_select in valid_options:
        valid_selection(usr_select)
    else:
        error()


while True:
    main_code()
