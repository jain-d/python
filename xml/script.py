import sys
import xml.etree.ElementTree as ET


xml_data = ET.parse("./test.xml")

xml_root = xml_data.getroot()
list_of_books = xml_root.findall("book")
print(type(list_of_books), list_of_books)

xml_root.remove(list_of_books[0])
book_name, book_author, book_year = sys.argv[1:]

new_book: ET.Element = ET.Element("book")
title: ET.Element = ET.Element("title")
title.text = book_name
author: ET.Element = ET.Element("author")
author.text = book_author
year = ET.Element("year")
year.text = book_year

new_book.append(title)
new_book.append(author)
new_book.append(year)

xml_root.append(new_book)

xml_data.write("./test.xml", encoding="utf-8", xml_declaration=True)
