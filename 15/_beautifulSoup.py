html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
    <title>My First Web Page</title>
</head>
<body>
    <h1 id="header">
        Python Course
    </h1>

    <div class="group1">
        <h2>
            Programming
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <div class="group2">
        <h2>
            Modules
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <div class="group3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <img src="test.jpg" alt="">
    
    <a class="sister" href="https://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="https://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="https://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")  # html dokumanini duzenler

# result = soup.prettify()
# result = soup.title
# result = soup.head
# result = soup.body
#
# result = soup.title.name
# result = soup.title.string
#
# result = soup.h1
# result = soup.h2
# result = soup.h2.name
# result = soup.h2.string
# result = soup.h1.string
#
# result = soup.find_all("h2")
# result = soup.find_all("h2")[1]
#
# result = soup.div
# result = soup.find_all("div")[1]
# result = soup.find_all("div")[1].ul
# result = soup.find_all("div")[1].ul.li
# result = soup.find_all("div")[1].ul.find_all("li")
#
# result = soup.div.findChildren()
#
# result = soup.div.findNextSibling()
# result = soup.div.findNextSibling().findNextSibling()
# result = soup.div.findNextSibling().findPreviousSibling()

result = soup.find_all("a")
for link in result:
    print(link.get("href"))

# print(result)
