import re

text = r"""Welcome to the Regex Training Center! Let's start with some dates:
01/02/2021, 12-25-2020, 2021.03.15, 2022/04/30, 2023.06.20, and 2021.07.04. You can
also find dates with words: March 14, 2022, and December 25, 2020.

Now let's move on to some phone numbers:
(123) 456-7890, +1-800-555-1234, 800.555.1234, 800-555-1234, and 123.456.7890.
Other formats include international numbers: +44 20 7946 0958, +91 98765 43210.

Here are some email addresses to find:
[john.doe@example.com](mailto:john.doe@example.com), [jane_doe123@domain.org](mailto:jane_doe123@domain.org), [support@service.net](mailto:support@service.net), [info@company.co.uk](mailto:info@company.co.uk),
and [contact.us@my-website.com](mailto:contact.us@my-website.com). You might also find these tricky: [weird.address+spam@gmail.com](mailto:weird.address+spam@gmail.com),
"quotes.included@funny.domain", and [this.one.with.periods@weird.co.in](mailto:this.one.with.periods@weird.co.in).

Need some URLs to extract? Try these:
[http://example.com](http://example.com/), [https://secure.website.org](https://secure.website.org/), [http://sub.domain.co](http://sub.domain.co/),
[www.redirect.com](http://www.redirect.com/), and [ftp://ftp.downloads.com](ftp://ftp.downloads.com/). Don't forget paths and parameters:
https://my.site.com/path/to/resource?param1=value1&param2=value2,
http://www.files.net/files.zip, https://example.co.in/api/v1/resource, and
https://another-site.org/downloads?query=search#anchor.

Hexadecimal numbers appear in various contexts:
0x1A3F, 0xBEEF, 0xDEADBEEF, 0x123456789ABCDEF, 0xA1B2C3, and 0x0. You might also find these:
#FF5733, #C70039, #900C3F, #581845, #DAF7A6, and #FFC300. RGB color codes can be tricky:
rgb(255, 99, 71), rgba(255, 99, 71, 1).

For those interested in Social Security numbers, here's some data:
123-45-6789, 987-65-4321, 111-22-3333, 555-66-7777, and 999-88-7777. Note that Social
Security numbers might also be written like 123 45 6789 or 123456789.

Let's throw in some random sentences for good measure:

- The quick brown fox jumps over the lazy dog.
- Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- Jack and Jill went up the hill to fetch a pail of water.
- She sells seashells by the seashore.

Finally, let's include some special characters and numbers:
1234567890, !@#$%^&*()_+-=[]{}|;':",./<>?, 3.14159, 42, and -273.15.

That's it! I hope you find this useful for your regex training."""

print('')

def parce_txt():
    i = 0
    for email in re.findall(r'[\w\d_\.-]+@[\w\d_\.-]+\.\w+', text):
        print(email)
        i = i + 1

    print('')
    print('Кількість знайдених email:', i)
    print('')

    i = 0
    for date in re.findall(
           r'[\>\s](\d{4}[\.\-\/]\d{2}[\.\-\/]\d{2})'
           r'|[\>\s](\d{2}[\.\-\/]\d{2}[\.\-\/]\d{4})'
           r'|(\w+\s\d{2},\s\d{4})', text):

        if date[0] != '':
            print(date[0])
        else:
            if date[1] != '':
                print(date[1])
            else:
                if date[2] != '':
                    print(date[2])
        i = i + 1

    print('')
    print('Кількість знайдених дат:', i)
    print('')

    i = 0
    for phone in re.findall(
           r'([\+\(]\d{1,3}\)*[\s-]\d{2,5}[\s-]\d{2,5}[\s-]*\d*)'
           r'|(\d{3}[\.-]\d{3}[\.-]\d*)', text):

        if phone[0] != '':
            print(phone[0])
        else:
            if phone[1] != '':
                print(phone[1])
        i = i + 1

    print('')
    print('Кількість знайдених номерів тел.:', i)
    print('')


i = 0
for addr_url in re.findall(
        r'(\w{3,5}:\/\/[\w\d\/\.?=&-]*#*[\w\d\/?=&-]*)'
        r'|(w{3}[\w\d\/\.?=&-]*)', text):

    if addr_url[0] != '':
        print(addr_url[0])
    else:
        if addr_url[1] != '':
            print(addr_url[1])
    i = i + 1

print('')
print('Кількість знайдених посилань URL.:', i)
print('')

if __name__ == '__main__':
    parce_txt()
