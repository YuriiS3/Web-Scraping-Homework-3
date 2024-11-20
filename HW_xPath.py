import xml.etree.ElementTree as ET
from lxml import etree

def parse_html():
    with open('br_indeed_com.txt', mode='r') as f:
        html = f.read()

    tree = etree.HTML(html)

    xpath = './/input[@id="text-input-what"]'
    tag_a = tree.xpath(xpath)

    print(tag_a)

    xpath = './/input[@id="text-input-where"]'
    tag_a = tree.xpath(xpath)

    print(tag_a)


    xpath = './/button[@class="yosegi-InlineWhatWhere-primaryButton"]'
    tag_a = tree.xpath(xpath)

    print(tag_a)

if __name__ == '__main__':
    parse_html()
