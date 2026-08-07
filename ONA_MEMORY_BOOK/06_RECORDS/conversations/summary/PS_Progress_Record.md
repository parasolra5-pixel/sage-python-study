ONA Python Study 진행 기록
날짜

2026-08-06

프로젝트

Sage & ONA Project

현재 작업

PYTHON_STUDY / micro_examples 구조 설계 및 정리

1. 완료된 작업 ✅
   GitHub 저장소 구조 확인

Repository:

sage-python-study

현재 큰 구조:
sage-python-study

├── ONA_IDEAS
│
├── ONA_MEMORY_BOOK
│
├── ONA_Mini_Python
│
├── ONA_Social_Worker
│
└── PYTHON_STUDY

2. PYTHON_STUDY 진행 상태

현재 구조:

PYTHON_STUDY
│
├── micro_examples
│
├── practice
│
└── projects

3. micro_examples 정리 완료 상태 ✅

기존에 잘못 생성된 하위 폴더와 파일 위치 문제를 정리함.

현재 기본 뼈대:

micro_examples
│
├── README.md
├── index.json
│
├── 01_basics
├── 02_strings
├── 03_numbers
├── 04_conditions
├── 05_loops
├── 06_data_structures
├── 07_functions
├── 08_modules
├── 09_files
├── 10_object_oriented
├── 11_errors
├── 12_ai_python
└── 99_ona_system

4. micro_examples 설계 목적

단순 Python 공부 폴더가 아니라:

작은 Python 예제
↓
정보 저장(info.json)
↓
index.json 관리
↓
ONA Mini Python
↓
python_dictionary.py
↓
학습 UI 표시

5. ONA Mini Python 연결 방향

관련 프로젝트:

ONA_Mini_Python

├── main.py
├── ui.py
├── theme.py
└── python_dictionary.py

6. 다음 작업 예정 🔜
   Step 1

01_basics부터 실제 예제 구조 만들기

예상 구조:

01_basics

├── variables
│
│ ├── variable_basic
│ │ ├── example.py
│ │ ├── info.json
│ │ └── README.md
│
├── input_output
│
└── comments

7. 중요한 결정 사항
   기존 방식

string_basic.py
if_basic.py

처럼 파일만 모으는 방식 ❌

변경 방식

개념 폴더
↓
예제 폴더
↓
example.py
info.json
README.md

방식으로 확장 가능하게 설계.

8. 현재 세이지가 직접 완료한 부분

✅ GitHub 저장소 정리
✅ ONA_MEMORY_BOOK 구성
✅ ONA Mini Python 위치 유지
✅ PYTHON_STUDY 생성
✅ micro_examples 생성
✅ 큰 카테고리 트리 생성
✅ 중복 폴더 제거

다음 창에서 이어갈 키워드

ONA Python Study 이어서

현재:
PYTHON_STUDY/micro_examples
큰 구조 완료

다음:
01_basics 내부 구조 만들기
ONA Mini Python python_dictionary.py 연결 설계
