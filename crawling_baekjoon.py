from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re
import sys


# URL을 통해 request요청을 보낸 후 html값을 받아온다.
def requestURL(number):
    url = "https://www.acmicpc.net/problem/" + number
    response = urlopen(url)
    html = soup(response, 'html.parser')

    return html

# html 코드로부터 문제 번호를 찾아온다.


def findProblemNumber(html):
    number = html.find('span', {'class': 'printable'}).text
    number = re.findall("\d+", number)
    number = number[0]

    return number

# html 코드로부터 문제 이름을 찾아온다.


def findProblemName(html):
    title = html.find('span', {'id': "problem_title"}).text
    problem = html.find('div', {'id': 'problem_description'})
    list = problem.findAll('p')

    return title

# html 코드로부터 문제 내용


def findProblemContent(html):
    problem = html.find('div', {'id': 'problem_description'})
    list = problem.findAll('p')

    content = ""
    for i in list:
        content += i.text.strip() + '\n'

    return content


# html 코드로부터 입력에 대한 정보를 가져온다.
def findInput(html):
    problem_input = html.find('div', {'id': 'problem_input'}).text.strip()

    return problem_input


# html 코드로부터 출력에 대한 정보를 가져온다.
def findOutput(html):
    problem_output = html.find('div', {'id': 'problem_output'}).text.strip()

    return problem_output


# 파일을 열어준다.
f = open('README.md', 'w')
# number = input()
number = str(sys.argv[1])
html = requestURL(number)

# 틀 만들어주기
content = '# 백준 '+findProblemNumber(html) + \
    ' - ' + findProblemName(html) + '\n\n'
content += '## 문제\n' + findProblemContent(html) + '\n\n'
content += '## 입력\n' + findInput(html) + '\n\n'
content += '## 출력\n' + findOutput(html) + '\n\n'

# 파일에 내용을 써주기
f.write(content)

# 파일 닫아주기
f.close()
