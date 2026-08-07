📖 ONA Project Continuation Note
프로젝트

sage-python-study

GitHub 저장소:
https://github.com/parasolra5-pixel/sage-python-study

현재 작업:
ONA Micro Structure Generator 개발

기준 문서:

ONA_MEMORY_BOOK/ONA_MEMORY_BOOK.md
ONA_MEMORY_BOOK/ONA_PROJECT_CONTEXT.md

1. ONA 프로젝트 방향

ONA는 단순한 코드 모음이 아니라:

작은 코드 예제를 모아 지식 라이브러리로 성장하는 학습 시스템

을 목표로 한다.

핵심 철학:

작은 것부터 만든다.
이해를 우선한다.
코드를 재사용 가능한 형태로 관리한다.
Python 학습과 ONA Mini Python UI로 연결한다.
기록을 남기며 성장한다. 2. 현재 GitHub 구조
sage-python-study

├─ONA_MEMORY_BOOK
│ ├─ONA_CORE_MEMORY.md
│ ├─ONA_MEMORY_BOOK.md
│ ├─ONA_PROJECT_CONTEXT.md
│
├─ONA_Mini_Python
│
├─ONA_Social_Worker
│
└─PYTHON_STUDY
│
├─micro_examples
│ ├─index.json
│ │
│ └─01_basics
│ └─variables
│ ├─001_variable_create.py
│ ├─002_variable_change.py
│ ├─003_multiple_variables.py
│ ├─README.md
│ └─metadata.json
│
└─tools
│
├─new
│ ├─create_micro_structure.py
│ └─micro_template.json
│
└─old
└─create_micro_structure.ps1 3. 지금까지 만든 것
v0.1
파일 자동 생성기

목표:

template
↓
Python 파일 생성

결과:

001_variable_create.py
002_variable_change.py
003_multiple_variables.py
v0.2
metadata 생성 추가

생성 결과:

variables
├─Python 파일
├─README.md
└─metadata.json

metadata:

{
"category": "01_basics",
"topic": "variables",
"description": "Python 변수 기본 예제",
"level": "beginner",
"examples": [
"variable_create",
"variable_change",
"multiple_variables"
]
}
v0.3
index.json 생성

목적:

ONA가 전체 자료 위치를 알 수 있게 함.

생성:

micro_examples/index.json

내용:

[
{
"category": "01_basics",
"topic": "variables",
"description": "Python 변수 기본 예제",
"level": "beginner",
"path": "01_basics/variables"
}
]
v0.4 (현재 완료)
index에 파일 목록 자동 등록

create_micro_structure.py 개선 완료.

현재 기능:

template
↓
폴더 생성
↓
.py 생성
↓
README 생성
↓
metadata 생성
↓
index.json 업데이트

실행 성공:

이미 존재: ../../micro_examples\01_basics\variables\001_variable_create.py
이미 존재: ../../micro_examples\01_basics\variables\002_variable_change.py
이미 존재: ../../micro_examples\01_basics\variables\003_multiple_variables.py
index.json 업데이트 완료 4. 현재 create_micro_structure.py 상태

기능:

Python 파일 자동 생성
README 자동 생성
metadata.json 자동 생성
index.json 자동 업데이트
기존 파일 보호
기존 index 항목 업데이트

중요 함수:

create_structure()

create_python_files()

create_readme()

create_metadata()

update_index() 5. 다음 목표
v0.5 예정

목표:

생성기를 더 안정화.

추가 예정:

JSON 오류 복구 기능
index 중복 관리 개선
metadata와 index 구조 통합 검토
여러 topic 자동 생성 테스트 6. 장기 목표

최종 구조:

ONA Mini Python

        ↓

index.json 읽기

        ↓

자동 메뉴 생성

        ↓

Python Micro Example 학습 UI

예:

Python 기초

├─ 변수
│ ├─ 변수 만들기
│ ├─ 변수 변경
│ └─ 여러 변수

├─ 문자열

├─ 조건문

└─ 반복문 7. 다음 온아에게 전달할 말

"온아, 우리는 sage-python-study에서 ONA Micro Structure Generator를 만들고 있어.
현재 v0.4까지 완료했고 index.json에 Python 파일 목록 자동 등록까지 성공했어.
이 기록을 기준으로 v0.5 안정화 단계부터 이어가자."
