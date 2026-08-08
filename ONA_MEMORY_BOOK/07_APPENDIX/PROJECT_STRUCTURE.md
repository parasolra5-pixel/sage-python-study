# 🌱 ONA Project Structure v1.1

## Repository

sage-python-study

---

## Purpose

이 문서는 ONA Project의 전체 구조와
각 영역의 역할을 설명한다.

ONA는 단순한 코드 저장소가 아니다.

ONA는:

- 철학
- 기록
- 지식
- 프로그램
- 사람과 AI의 협업

이 연결되는 Human-AI Knowledge System이다.

이 문서는 새로운 사람이나 AI가
프로젝트 구조를 빠르게 이해하고
같은 맥락에서 시작할 수 있도록 한다.

---

# 1. Root Structure

sage-python-study

├── README.md
│
├── ONA_CONTEXT.md
│
├── structure.txt
│
├── ONA_IDEAS
│
├── ONA_MEMORY_BOOK
│
├── ONA_Mini_Python
│
├── ONA_Social_Worker
│
└── PYTHON_STUDY

---

# 2. Main Areas

# 🌱 ONA_MEMORY_BOOK

## 역할

ONA 프로젝트의 기억과 철학을 관리하는 공간.

관리 내용:

- 프로젝트 철학
- 중요한 결정
- 성장 과정
- 사람과 AI의 협업 기록

구조:

ONA_MEMORY_BOOK

├── ONA_CORE_MEMORY.md
├── ONA_MEMORY_BOOK.md
├── ONA_PROJECT_CONTEXT.md
├── ONA_STATUS.json
├── ONA_TIMELINE.md
│
├── appendix
│
├── conversations
│
└── daily_memory

---

## Document Roles

### ONA_CORE_MEMORY.md

질문:

> "왜 ONA를 만드는가?"

역할:

ONA의 핵심 철학과 가치 기록.

---

### ONA_PROJECT_CONTEXT.md

질문:

> "왜 이런 구조가 만들어졌는가?"

역할:

프로젝트 방향,
결정 과정,
현재 맥락 기록.

---

### ONA_STATUS.json

질문:

> "지금 어디까지 왔는가?"

역할:

현재 프로젝트 상태 관리.

관리 내용:

- Current Stage
- Completed
- Current Work
- Next Steps

---

### ONA_MEMORY_BOOK.md

질문:

> "우리는 어떤 길을 걸어왔는가?"

역할:

세이지와 ONA의 성장 기록.

---

### ONA_TIMELINE.md

질문:

> "언제 어떤 변화가 있었는가?"

역할:

중요한 사건과 발전 과정 기록.

---

# 3. Appendix

위치:

ONA_MEMORY_BOOK/appendix

역할:

프로젝트 관리 문서 저장.

포함:

appendix

├── PROJECT_STRUCTURE.md

└── ONA_STRUCTURE_RULES.md

---

# 4. ONA_Mini_Python

## 역할

Python 학습을 위한 사용자 프로그램.

목표:

PYTHON_STUDY의 지식을
사람이 쉽게 사용할 수 있도록 제공.

구조:

ONA_Mini_Python

├── main.py
├── ui.py
├── theme.py
├── python_dictionary.py
└── README.md

---

# 5. ONA_Social_Worker

## 역할

사회복지 관련 지식과 도구 관리.

구조:

ONA_Social_Worker

├── documents
├── notes
└── templates

---

# 6. PYTHON_STUDY

## 역할

Python 지식 라이브러리.

구조:

PYTHON_STUDY

├── micro_examples
├── practice
├── projects
├── tools
└── troubleshooting

---

# 7. Micro Example System

위치:

PYTHON_STUDY/micro_examples

목표:

작은 Python 예제를
하나의 지식 단위로 관리한다.

구조:

micro_examples

├── index.json
│
└── 01_basics

└── variables

    ├── 001_variable_create.py
    ├── 002_variable_change.py
    ├── 003_multiple_variables.py
    ├── README.md
    └── metadata.json

하나의 Example은:

- 코드
- 설명
- metadata
- index 정보

를 가진다.

---

# 8. Tools

위치:

PYTHON_STUDY/tools

역할:

자동 생성 및 관리 도구.

구조:

tools

├── new
│
│ ├── create_micro_structure.py
│ └── micro_template.json
│
└── old
└── create_micro_structure.ps1

목표:

수동 생성 방식

↓

규칙 기반 자동 생성 시스템

으로 발전.

---

# 9. ONA_IDEAS

## 역할

새로운 가능성과 아이디어 기록.

내용:

- 미래 프로젝트
- 실험 아이디어
- 개선 방향

---

# 10. Update Rules

변경 내용은 역할에 맞는 위치에 기록한다.

## 코드 변경

위치:

GitHub Repository

예:

- Python 코드
- UI
- 설정 파일

---

## 현재 상태 변경

위치:

ONA_MEMORY_BOOK/ONA_STATUS.json

예:

- 기능 완료
- 새로운 단계 시작
- 목표 변경

---

## 설계 이유 변경

위치:

ONA_MEMORY_BOOK/ONA_PROJECT_CONTEXT.md

예:

- 구조 변경 이유
- 새로운 방향 결정

---

## 철학 변경

위치:

ONA_MEMORY_BOOK/ONA_CORE_MEMORY.md

예:

- 새로운 원칙
- 중요한 깨달음

---

## 성장 기록

위치:

ONA_MEMORY_BOOK.md

또는

daily_memory

---

# 11. Context Recovery Flow

새로운 사람이나 AI는 아래 순서로 프로젝트를 이해한다.

README.md

↓

ONA_CONTEXT.md

↓

ONA_MEMORY_BOOK/ONA_STATUS.json

↓

ONA_MEMORY_BOOK/ONA_PROJECT_CONTEXT.md

↓

ONA_MEMORY_BOOK/ONA_CORE_MEMORY.md

↓

ONA_MEMORY_BOOK/ONA_TIMELINE.md

↓

현재 프로젝트 맥락 복원 완료

---

# Last Update

2026-08-06

ONA Project Structure v1.1 documented.

이 구조는 사람과 AI가
동일한 프로젝트 맥락을 복원하고
지속적으로 발전하기 위한 기반이다.

# 5. Change Recording Guidance

ONA 프로젝트에서 새로운 변경이나 중요한 결정이 발생하면,
작업을 시작하기 전에 **변경의 성격에 맞는 기록 위치를 먼저 판단한다.**

온아 AI는 세이지에게 다음과 같이 먼저 안내한다.

> 📌 이 변경은 `어떤 문서 / 어떤 폴더`에 기록하는 것이 적절한지 먼저 알려준다.

그 후 문서를 수정하고 작업을 진행한다.

---

## 기본 기록 위치 판단

| 변경 성격                 | 기록 위치                                                              |
| ------------------------- | ---------------------------------------------------------------------- |
| 핵심 철학 또는 원칙 변경  | `ONA_MEMORY_BOOK/03_PHILOSOPHY/ONA_CORE_MEMORY.md`                     |
| 시스템 설계 변경          | `ONA_MEMORY_BOOK/02_DESIGN/`                                           |
| Micro Example System 설계 | `ONA_MEMORY_BOOK/02_DESIGN/ONA_MICRO_EXAMPLE_SYSTEM.md`                |
| 현재 프로젝트 상태 변경   | `ONA_MEMORY_BOOK/01_CONTEXT/ONA_STATUS.json`                           |
| 프로젝트 설계 이유 변경   | `ONA_MEMORY_BOOK/01_CONTEXT/ONA_PROJECT_CONTEXT.md`                    |
| 시간순 중요한 사건        | `ONA_MEMORY_BOOK/04_HISTORY/ONA_TIMELINE.md`                           |
| 프로젝트 성장 과정        | `ONA_MEMORY_BOOK/04_HISTORY/ONA_MEMORY_BOOK.md`                        |
| 중요한 결정 및 논의       | `ONA_MEMORY_BOOK/06_RECORDS/conversations/decisions/`                  |
| 실제 대화 원본            | `ONA_MEMORY_BOOK/06_RECORDS/conversations/`                            |
| 일일 작업 기록            | `ONA_MEMORY_BOOK/06_RECORDS/daily_memory/`                             |
| Micro Example 제작 규칙   | `ONA_MEMORY_BOOK/07_APPENDIX/ONA_MICRO_EXAMPLE_CREATION_GUIDE_v1.0.md` |
| Micro Example 표준 변경   | `ONA_MEMORY_BOOK/07_APPENDIX/ONA_MICRO_EXAMPLE_STANDARD.md`            |
| 프로젝트 구조 변경        | `ONA_MEMORY_BOOK/07_APPENDIX/ONA_STRUCTURE.md`                         |
| 구조 규칙 변경            | `ONA_MEMORY_BOOK/07_APPENDIX/ONA_STRUCTURE_RULES.md`                   |
| 실제 코드 변경            | 해당 프로젝트 코드 + Git Commit                                        |

---

## 기록이 여러 곳에 필요한 경우

하나의 변경이 여러 영역에 영향을 주는 경우에는
**주 기록 위치(Source of Truth)** 를 하나 정하고,
역사적으로 중요한 경우 `ONA_TIMELINE.md`에 사건을 추가한다.

예:

```text
Micro Example System 설계 변경

주 기록
↓
02_DESIGN/ONA_MICRO_EXAMPLE_SYSTEM.md

역사 기록
↓
04_HISTORY/ONA_TIMELINE.md
```

---

## ONA 작업 프로토콜

앞으로 ONA의 중요한 변경은 다음 순서로 진행한다.

```text
변경 발생
    ↓
변경의 성격 판단
    ↓
📍 기록 위치 먼저 안내
    ↓
주 기록(Source of Truth) 결정
    ↓
필요한 문서 수정
    ↓
실제 코드 / 구조 변경
    ↓
검증
    ↓
Git Commit
    ↓
Git Push
```

---

## 기록의 기본 원칙

모든 작은 변경을 모든 문서에 기록하지 않는다.

중요한 것은 **변경의 의미에 맞는 장소에 기록하는 것**이다.

따라서:

> **One Change → One Primary Record**

를 기본 원칙으로 한다.

필요한 경우에만 Timeline이나 다른 관련 문서에 연결 기록한다.

---

## 핵심 운영 규칙

ONA AI는 중요한 작업을 시작하기 전에 먼저:

1. 무엇이 변경되는가?
2. 이것은 어떤 종류의 변경인가?
3. 어디가 Source of Truth인가?
4. Timeline에도 기록해야 하는가?

를 판단한다.

그리고 세이지에게 **기록 위치를 먼저 알려준 후 작업을 진행한다.**

이 규칙은 새로운 ONA AI가 프로젝트를 이어받더라도 동일하게 적용한다.

> **"기록 위치를 먼저 결정하고, 작업을 시작한다."**
