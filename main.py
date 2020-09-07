import sys
import turtle
from styles import *

TITLE = ""
STYLE = Styles("", "", "green", "Times New Roman")


def paragraph_image_loop():
    to_write = []
    while True:
        paragraph_answer = parse_answer(input("Do you want to add a another paragraph? [yes] "))
        if paragraph_answer:
            to_write.append(
                paragraph_html(input("Title of your paragraph: "), input("Content of your paragraph (single line)\n")))
        image_answer = parse_answer(input("Do you want to add images? [yes] "))
        if image_answer:
            to_write.append(image_html(input('Image file name: ')))
        if (paragraph_answer and image_answer) is False:
            return to_write


def parse_answer(answer):
    """
    Checks the user's :param answer:. If the answer is "yes" or an empty string, :return True. If the answer is
    something else, it will :return False.
    :param answer: string
    :return: True or False
    """
    if answer == "yes" or answer == "":
        return True
    else:
        return False


def handle_fonts(answer):
    """
    This function checks to see if the :param answer: is "yes" or an empty string. If so, a turtle window will display
    the different types of fonts. If another string, the user will select a font by it's number in the output window.
    :param answer: string
    :return: fonts
    """
    fonts = ["Arial", "Comic Sans MS", "Lucida Grande", "Tahoma", "Verdana", "Helvetica", "Times New Roman"]
    if answer:
        turtle.Screen().setup(width=650, height=650)
        turtle.delay(0)
        turtle.up()
        turtle.hideturtle()
        turtle.setpos(-230, 250)
        turtle.right(90)
        for font in fonts:  # writes all of the fonts within the turtle window.
            turtle.write(font, font=(font, 14, "normal"), align='center')
            turtle.forward(50)
        turtle.Screen().exitonclick()
        return handle_fonts(False)  # recursive call of function.
    else:
        print("Please select a font by its number.")
        for index in range(len(fonts)):  # goes through the lists of fonts and displays them.
            print(str(index) + ":" + fonts[index] + ", size 14")  # prints the fonts.
        return fonts[int(input(">> "))]  # returns an input asking for a number the user inputs corresponding with the
        # font.


def write_file(text, filename="index"):
    """
    Opens and writes a :param filename: as an html file and writes to the :param text.
    :param text: string
    :param filename
    """
    f = open(filename + ".html", "w")
    for item in text:
        f.write(item)
    print("Your website has been saved: " + filename + ".html")


def wizard_mode():
    """
    Wizard mode appends the contents to a web page to an empty list. Lastly, it writes the file.
    """
    to_write = []
    to_write.append(header_html())
    title = (input("What is the title of your website? "))
    to_write.append(title_html(title))
    to_write.insert(1, h1_html(title))
    STYLE.background_color = input("Background Color\nChoose the name of a color, or in format '#XXXXXX': ")
    STYLE.font_style = handle_fonts(
        parse_answer(input("You will now choose a font.\nDo you want to see what the font looks like? [yes] ")))
    STYLE.font_color = input("Paragraph Text Color\nChoose the name of a color, or in format '#XXXXXX': ")
    STYLE.heading_color = input("Heading Color\nChoose the name of a color, or in format '#XXXXXX': ")
    to_write.append(
        paragraph_html(input("Title of your paragraph: "), input("Content of your paragraph (single line)\n")))
    if parse_answer(input("Do you want to add images? [yes] ")):
        to_write.append(image_html(input("Image file name: ")))
    to_write += paragraph_image_loop()
    to_write.append(end_html())
    to_write.insert(2, style_html(STYLE))
    write_file(to_write)


def web_mode():
    STYLE.background_color = input("Background Color\nChoose the name of a color, or in format '#XXXXXX': ")
    STYLE.font_style = handle_fonts(
        parse_answer(input("You will now choose a font.\nDo you want to see what the font looks like? [yes] ")))
    STYLE.font_color = input("Paragraph Text Color\nChoose the name of a color, or in format '#XXXXXX': ")
    STYLE.heading_color = input("Heading Color\nChoose the name of a color, or in format '#XXXXXX': ")
    args = sys.argv
    titles = []
    websites = []
    for filename in args[1:]:
        to_write = [header_html()]
        read1 = read_file(filename)
        curr_title = read1[0].strip()
        titles.append(curr_title)
        to_write.append(title_html(read1[0].strip()))
        i = 1
        while i < len(read1):
            if read1[i] == "!new_paragraph":
                title = read1[i + 1][7:]
                paragraph = read1[i + 2]  # debug
                to_write.append(paragraph_html(title, paragraph))
                i += 2
            else:
                to_write.append(image_html(read1[i][7:-4], read1[i][-3:]))
                # print("Image: " + read1[i][7:-3] + read1[i][-3:])
            i += 1
        to_write.append(end_html())
        to_write.insert(1, h1_html(curr_title))
        to_write.insert(2, style_html(STYLE))
        websites.append(to_write)
    links = link(titles)
    for i in range(len(titles)):
        websites[i].insert(3, links)
    for i in range(len(titles)):
        write_file(websites[i], titles[i])


def read_file(file_name):
    read_list = []
    text = ""
    f = open(file_name)
    for line in f:
        line = line.strip("\n")
        if line == "":
            pass
        elif line[0] == '!':
            print(line)
            if len(text) > 0:
                read_list.append(text)
                text = ""
            read_list.append(line)
        else:
            text += line
    if len(text) > 0:
        read_list.append(text)
    f.close()
    return read_list


def main():
    if len(sys.argv) == 1:
        wizard_mode()
    else:
        web_mode()


main()
