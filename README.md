# 귀찮아서 만들어본 스크립트 파일들

매번 같은 명령어를 반복해서 치다 보니깐 한번에 할 수 있는 방법이 없을까 해서 만들었습니다.

- [백준 사이트에서 간단하게 문제를 가져오게 하는 크롤링](description/crawling_baekjoon.md)

> python [크롤링 파일이 존재하는 경로] [문제번호]

- [cpp파일, md파일, txt파일 만들어주는 스크립트](description/vscode.md)

> 사용 방법 : vscode [문제 번호]

- [py파일, md파일, txt파일 만들어주는 스크립트](description/pycode.md)

> 사용 방법 : pycode [문제 번호]

## 간단하게 만들어보기
맥이나 우분투 사용자의 경우 alias를 통해 간단하게 간단하게 설정해 놓을 수 있다.

> alias crawling="python $HOME/dev/script/crawling_baekjoon.py"

이렇게 해 놓음으로써 `crawling`이라는 명령어를 만들었다.
