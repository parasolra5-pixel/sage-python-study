# ONA Micro Example Creation Guide v1.0

## 0. Purpose

ONA Micro Example Creation Guide는
Python 학습 지식을 만드는 사람이
일관된 기준으로 작은 학습 예제를 제작하기 위한 가이드이다.

Micro Example은 단순한 코드 파일이 아니다.

하나의 Micro Example은:

- 하나의 Python 개념
- 실행 가능한 코드
- 이해하기 쉬운 설명
- 학습 목표
- 지식 연결 정보

를 가진 하나의 작은 지식 단위이다.

---

# 1. Basic Principle

ONA Micro Example의 핵심 원칙:

## Understand First

코드를 보여주기 전에
왜 필요한지 이해한다.

## Build Small

하나의 예제는 하나의 개념만 다룬다.

## Explain Clearly

초보자가 이해할 수 있는 언어로 설명한다.

## Connect Knowledge

각 예제는 다른 지식과 연결될 수 있도록 기록한다.

---

# 2. Micro Example Definition

Micro Example:

하나의 Python 개념을 학습하기 위한
독립 실행 가능한 작은 프로그램이다.

예:

좋은 예:
001_create_variable.py

목표:

변수를 만들고 값을 저장하는 방법 이해

좋지 않은 예:

001_python_basic_all.py

내용:

변수 + 조건문 + 반복문 + 함수

하나의 예제에 너무 많은 개념을 포함하지 않는다.

---

# 3. Example Size Rule

하나의 Micro Example은:

- 5~30줄 정도의 작은 코드
- 외부 라이브러리 사용하지 않음
- 다른 파일 없이 실행 가능
- 결과를 쉽게 예측 가능

을 기본으로 한다.

---

# 4. Learning Order

예제는 항상 쉬운 것부터 어려운 것으로 구성한다.

기본 흐름:

개념 소개
↓
기본 사용
↓
변형 사용
↓
응용 연결

예:

변수:

001_variable_create

변수 만들기

↓

002_variable_change

값 변경하기

↓

003_multiple_variables

여러 변수 사용하기

---

# 5. Code Writing Rules

## 파일 이름

형식:

001_example_name.py

규칙:

- 세 자리 숫자 사용
- snake_case 사용
- 기능이 드러나는 이름 사용

---

## 코드 작성

모든 예제는:

- 한국어 주석 포함
- 초보자가 읽을 수 있는 코드
- 불필요한 축약 사용 금지

예:

```python
# 이름이라는 변수를 만들고 문자열을 저장합니다.

name = "Sage"

print(name)
6. Explanation Style

ONA 설명 방식:

단순한 정의보다 원리를 설명한다.

예:

일반 설명:

"변수는 값을 저장하는 공간입니다."

ONA 설명:

"변수는 데이터를 기억하기 위한 이름표입니다.
컴퓨터 메모리에 있는 값에 사람이 이해하기 쉬운 이름을 붙여 사용하는 방법입니다."

7. Metadata Writing Rule

metadata.json은
ONA Knowledge System이 읽는 정보이다.

반드시 포함:

title
description
learning_objectives
prerequisites
examples

예제 정보:

무엇을 배우는가
왜 필요한가
어디에 연결되는가

를 기록한다.

8. Topic Organization

Topic은 하나의 학습 주제를 의미한다.

예:

01_basics

variables

comments

operators

하나의 Topic에는:

README.md

metadata.json

001_example.py

002_example.py

구조를 유지한다.

9. Connection Rule

새로운 Example을 만들 때 생각한다.

질문:

이것은 어떤 지식과 연결되는가?
이전에 배운 것은 무엇인가?
다음에는 무엇으로 이어지는가?

예:

variables

↓

input

↓

conditions

↓

functions

지식은 나무처럼 성장한다.

10. ONA Philosophy

ONA Micro Example은
많은 코드를 모으는 것이 목적이 아니다.

작은 이해를 쌓아
큰 지식 구조를 만드는 것이 목적이다.

하나의 작은 예제가

하나의 지식 씨앗이 되고,

연결된 씨앗들이

ONA Knowledge System을 만든다.

Version History
v1.0

2026-08-07

초기 작성.

ONA Micro Example 제작 기준 정립.
```
