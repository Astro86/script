#!/bin/zsh

mkdir $1
cd $1

file=pwd
#file+="/$1"

# 마크다운 파일에 관한 함수
if [ -f $file/README.md ]; then
    code README.md
else
    touch README.md
#    python $HOME/dev/crawling_baekjoon.py $1
    code README.md
fi

# 입력을 위한 txt파일 생성
if [ -f $file/data.txt ]; then
    code data.txt
else
    touch data.txt
    code data.txt
fi


# cpp 파일 생성
if [ -f $file/$1.cpp ]; then
    code $1.cpp
else
    touch $1.cpp
    code $1.cpp
fi


#
## 파일 생성
#touch data.txt
#touch $1.cpp
#
## 파일 열기
#code data.txt
#code $1.cpp
#
#
#python $HOME/dev/crawling_baekjoon.py $1
