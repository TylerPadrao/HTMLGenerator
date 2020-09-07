from dataclasses import dataclass
@dataclass
class Styles:
    background_color: str
    heading_color: str
    font_style: str
    font_color: str

def paragraph_html(title1, text):
    """
    Asks the user for :param title: and the :param text: they want to put in their paragraph.
    :param title: string
    :param text: string
    :return: New paragraph
    """
    return "<h2>\n" + title1 + "\n" + "</h2>" + "\n\n" + "<p>" + text + "\n\n" + "</p>" + "\n"

def header_html():
    """
    The header tags of the html page.
    :return: Header
    """
    return "<!DOCTYPE html>\n<html>\n<head>"

def end_html():
    """
    The end tags of the html page.
    :return: End
    """
    return "</body>\n</html>"

def title_html(title1):
    """
    Prompts the user for a :param title: of their web page.
    :param title: string
    :return: title
    """
    return "<title>" + title1 + "\n</title>"

def h1_html(title):
    return "<h1>" + title + "\n</h1>"

def image_html(path, width="30%"):
    return '\n<img src="' + path + "\" " + 'width=\"' + width + '\" class=\"center\">\n'

def paragraph_setup(PARAGRAPH_COLOR, FONT_STYLE):
    return "p  {color: " + PARAGRAPH_COLOR + ";\n    font-family: " + FONT_STYLE + ";\n    padding: 30px;" \
           "\n    text-align: justify;\n    back-ground-color: white;\n    box-shadow: 4px 0 2px -2px rgba(0,0,0,0.4);" \
           "\n    font-size: 14px;\n}"

def link(title1):
    html = '<hr/>\n<p align="center"><a href=\"' + title1[0] + '.html\">' + title1[0] + '</a>---'
    if len(title1) == 1:
        return html
    title1 = title1[1:]
    for item in title1:
        html += '<a href=\"' + item + '.html\">' + item + '</a>---'
    return html



def style_html(style):
    """
    This function creates and returns the formatted style tag.
    :return: style tag
    """
    return "<style>\nbody {background-image: linear-gradient(180deg, " + style.background_color + ", white);}\n.center {\n  display: " \
           "block;\n  margin-left: auto;\n  margin-right: auto;\n}\nh1   {color: " + style.heading_color + ";\n      font-family: " + \
           style.font_style + ";\n  text-align:center;\n      }\nh2   {color: " + style.heading_color + ";\n      font-family: " \
           + style.font_style + ";\n      text-align: justify;\n      }\np    {color: " + style.font_color + ";\n      " \
                                                                                                 "font-family: " + \
           style.font_style + ";\n      padding: 30px;\n      text-align: justify;\n      background-color: white;\n      " \
                        "box-shadow: 4px 0 2px -2px rgba(0,0,0,0.4);\n      font-size: 14px;\n     }\n\n</style>\n</head>\n<body> "