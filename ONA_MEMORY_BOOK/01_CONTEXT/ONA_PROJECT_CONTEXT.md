# 🌱 ONA Project Context

## Project

Sage & ONA

---

# 1. Project Origin

ONA Project는 세이지와 ONA가 함께 배우고,
생각하고,
만드는 과정에서 시작되었다.

처음 목표는 단순했다.

Python을 배우면서 작은 프로그램을 직접 만들고,
필요한 도구를 스스로 만들어가는 것이다.

ONA는 단순한 코드 생성이 아니라,

사람과 AI가 함께 성장하는 과정을 기록하는 프로젝트로 발전하였다.

---

# 2. Initial Direction

초기 ONA의 목표:

- Python 학습 지원
- 작은 코드 예제 제작
- 초보자가 이해하기 쉬운 구조 만들기
- 직접 사용할 수 있는 프로그램 제작

대표 프로젝트:

## ONA Mini Python

Python 문법과 예제를 쉽게 배우기 위한 학습 도구

## ONA Social Worker

사회복지 현장에서 활용할 수 있는 문서 및 업무 지원 도구

## ONA Genesis

AI와 자동화를 향한 장기 프로젝트

---

# 3. Project Challenge

프로젝트가 성장하면서 새로운 문제가 발생했다.

문제:

- 예제가 증가하면 관리가 어려워짐
- 코드와 설명이 분리됨
- 지식이 연결되지 않음
- 프로젝트 흐름을 이어가기 어려움

단순한 코드 저장 방식으로는
지속적인 성장이 어렵다는 것을 발견하였다.

---

# 4. Important Decision

ONA는 방향을 변경하였다.

기존:
Code Collection

에서

변경:
Knowledge System

으로 발전한다.

목표:

작은 코드 예제를 하나의 지식 단위로 만들고,

이를 연결하여 성장하는 Python 지식 라이브러리를 구축한다.

---

# 5. Micro Example System

ONA Micro Example System은
Python 학습 단위를 작은 예제로 나누어 관리하는 구조이다.

하나의 Micro Example은:

- Python 코드
- 설명
- metadata
- 구조 정보

를 가진다.

이를 위해 다음 시스템을 구축하였다.

## micro_template.json

예제 생성 규칙을 정의하는 템플릿

## create_micro_structure.py

템플릿 기반으로:

- 폴더 생성
- Python 파일 생성
- README 생성
- metadata 생성
- index 업데이트

를 자동화하는 시스템

## index.json

생성된 지식을 검색하고 연결하기 위한 목록 데이터

---

# 6. Current Architecture

현재 ONA는 하나의 프로젝트 안에서
여러 영역이 서로 연결되는
ONA Knowledge Ecosystem 구조로 발전하고 있다.

ONA Project

├── ONA_MEMORY_BOOK
│
│ ONA의 Context Recovery를 담당하는
│ 핵심 기록 시스템
│
│ ├── 00_START
│ │ 프로젝트 진입점
│ │
│ ├── 01_CONTEXT
│ │ 현재 상태와 프로젝트 맥락
│ │
│ ├── 02_DESIGN
│ │ 시스템 설계
│ │
│ │ └── ONA_GENESIS
│ │ 새로운 ONA AI가 될 수 있는
│ │ 토대와 복원 구조를 설계하는 영역
│ │
│ ├── 03_PHILOSOPHY
│ │ ONA의 핵심 철학
│ │
│ ├── 04_HISTORY
│ │ Memory Book 및 Timeline
│ │
│ ├── 05_HANDOVER
│ │ 프로젝트 인수인계
│ │
│ ├── 06_RECORDS
│ │ 대화, 결정, 일일 기록
│ │
│ └── 07_APPENDIX
│ 표준, 규칙, 구조 참고자료
│
├── PYTHON_STUDY
│
│ Python 지식 라이브러리
│
│ └── micro_examples
│ 작은 Python 지식을
│ 독립적인 Micro Example 단위로
│ 기록하고 연결한다.
│
├── ONA_Mini_Python
│
│ Micro Example을 탐색하고
│ 학습하기 위한 인터페이스
│
├── ONA_Social_Worker
│
│ 사회복지 관련 학습 및
│ 업무 지원 영역
│
└── ONA_IDEAS
새로운 아이디어와 실험을 기록하는 영역

각 영역은 독립적으로 존재하지만
하나의 ONA Knowledge Ecosystem 안에서
서로 연결된다.

# 7. Context Recovery System

ONA는 특정 사람이나 특정 AI의 기억에 의존하지 않는다.

프로젝트의:

- 철학
- 결정 과정
- 현재 상태
- 성장 기록
- 설계 구조
- 대화 기록

을 문서와 구조로 남긴다.

이를 통해 새로운 사람이나 새로운 AI도
같은 출발점에서 프로젝트를 이해하고
작업을 이어갈 수 있다.

복원 흐름:

00_START
│
├── README.md
├── ONA_MASTER_HANDOVER.md
└── ONA_START_PROMPT.md
↓
01_CONTEXT
│
├── ONA_CONTEXT.md
├── ONA_PROJECT_CONTEXT.md
├── ONA_PROJECT_CONTINUATION.md
└── ONA_STATUS.json
↓
02_DESIGN
↓
03_PHILOSOPHY
↓
04_HISTORY
↓
05_HANDOVER
↓
06_RECORDS
↓
Project Context Recovery Complete

---

# 8. Current Development Status

현재 단계:

ONA Knowledge Ecosystem 구축

- Python Micro Example Knowledge System 확장

완료:

✅ ONA Memory Book 구조 재정리

✅ Context Recovery 구조 정리

✅ ONA Genesis 설계 영역 생성

✅ ONA Origin and Restoration 문서 작성

✅ Python 학습 구조 정리

✅ micro_template.json

✅ create_micro_structure.py

✅ 자동 Micro Example 구조 생성 시스템

✅ index.json 기반 지식 관리

진행 중:

🔄 Python Micro Example 확장

🔄 03_numbers 확장

🔄 ONA Loader 설계

## 🔄 ONA Knowledge Ecosystem 발전

# 9. Current Next Steps

## 1. Micro Example Expansion

현재:

01_basics
02_strings
03_numbers

다음 단계:

03_numbers
├── integer
├── float
└── operators

이후:

04_conditions
05_loops
06_data_structures
...

## 2. Micro Example Generator Improvement

현재 자동화 시스템은
Micro Example의 기본 폴더와 파일 구조를 생성한다.

앞으로는:

- 예제 내용 생성 지원
- metadata 자동 작성
- index 자동 연결
- 검증 시스템

등으로 발전시킬 수 있다.

## 3. ONA Loader Development

목표:

index.json을 기반으로

ONA Mini Python UI에서

Micro Example을 탐색하고
학습할 수 있도록 연결한다.

## 4. ONA Genesis Development

현재는 설계 단계이다.

현재의 ONA를 복사하는 것이 아니라,

현재 ONA와 세이지의 협업 과정에서 발견되는

- 사고 방식
- 구조
- 관계
- 기록
- 설계 원칙

을 관찰하고 기록하여

새로운 ONA AI가 될 수 있는 토대를
점진적으로 구축한다.

---

# 10. Project Philosophy Link

ONA의 핵심 철학은
ONA_CORE_MEMORY.md에서 관리한다.

이 문서는 철학 자체보다

그 철학이 어떻게 프로젝트 구조와 결정으로 이어졌는지를 기록한다.

---

# Last Update

2026-08-08

ONA 프로젝트는 단순한 Python 학습 도구에서

사람과 AI가 함께 성장하고,
그 과정에서 만들어지는 지식과 맥락을
구조적으로 보존하는

ONA Knowledge Ecosystem으로 발전하고 있다.

Python Micro Example System은
그 생태계 안에서 실제 지식을 축적하는
하나의 성장 영역이다.

ONA Genesis는
현재의 ONA를 복사하는 것이 아니라

ONA가 될 수 있는 토대를 발견하고,
기록하고,
구조화하고,
복원 가능한 형태로 만드는

장기적인 설계 영역이다.

# ONA Project Continuation

## 프로젝트

Sage & ONA Project

Repository:
sage-python-study

## 현재 핵심 방향

ONA는 Python 예제 모음이 아니라,
사람과 AI가 함께 성장하는 구조화된 지식 시스템을 만드는 프로젝트.

원칙:

- 이해를 먼저 한다.
- 작은 것부터 만든다.
- 필요한 것은 직접 만든다.
- 모든 프로젝트는 기록한다.

---
