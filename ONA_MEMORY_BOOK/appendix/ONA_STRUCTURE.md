# 🌱 ONA Structure

## ONA Project Architecture v1.0

> ONA는 사람과 AI가 함께 성장하는 Human-AI Collaborative Knowledge System이다.
>
> 이 문서는 ONA 프로젝트의 전체 구조와 각 구성 요소의 역할,
> 그리고 서로 어떻게 연결되는지를 설명한다.

---

# 1. ONA Structure Philosophy

ONA는 단순한 코드 저장소가 아니다.

ONA는:

- 생각을 기록하고
- 지식을 구조화하고
- 프로젝트의 맥락을 보존하며
- 사람과 AI가 함께 성장할 수 있도록 만드는

지식 생태계(Knowledge Ecosystem)이다.

ONA의 핵심 원칙:

```
Structure
    ↓
Record
    ↓
Connect
    ↓
Knowledge
    ↓
Emergence
```

구조가 먼저 만들어지고,
그 위에서 새로운 가능성이 성장한다.

---

# 2. Overall Architecture

ONA 전체 구조:

```
                         Sage
                  (Human Creator)
                             |
                             |
                             ▼

                    ONA Collaboration

                             |
        ------------------------------------------------
        |                                              |
        ▼                                              ▼


  ONA Memory System                         ONA Knowledge System

  (Context & History)                       (Learning & Creation)


        |                                              |
        |                                              |
        ▼                                              ▼


 ONA_MEMORY_BOOK                             PYTHON_STUDY

        |                                              |
        |                                              |
        ▼                                              ▼


 Philosophy                                 Micro Example System

 Design                                     Metadata System

 History                                    Learning Library

 Status                                     Automation Tools


```

---

# 3. ONA Memory System

## Purpose

ONA 프로젝트의 맥락(Context)을 보존하고 복원하기 위한 시스템이다.

ONA는 특정 AI의 기억에 의존하지 않는다.

대신:

- 문서
- 구조
- 기록

을 통해 프로젝트의 의미와 방향을 복원한다.

---

## Structure

```
ONA_MEMORY_BOOK

├── ONA_CONTEXT.md
│
├── ONA_CORE_MEMORY.md
│
├── ONA_PROJECT_CONTEXT.md
│
├── ONA_MEMORY_BOOK.md
│
├── ONA_TIMELINE.md
│
├── ONA_STATUS.json
│
└── appendix
    └── ONA_STRUCTURE.md
```

---

# 4. Document Responsibility

## README.md

역할:

프로젝트 소개

질문:

> ONA는 무엇인가?

---

## ONA_CONTEXT.md

역할:

프로젝트 시작점

담당:

- 프로젝트 이해 방법
- 문서 읽는 순서
- Context Recovery 방법

질문:

> 어떻게 ONA를 이해하는가?

---

## ONA_CORE_MEMORY.md

역할:

ONA 철학 관리

담당:

- Context Recovery Philosophy
- Structure Before Emergence
- Human-AI Collaboration

질문:

> 왜 ONA를 만드는가?

---

## ONA_PROJECT_CONTEXT.md

역할:

설계 과정 기록

담당:

- 문제 발견
- 방향 변경
- 구조 결정 이유

질문:

> 왜 이런 구조가 되었는가?

---

## ONA_STATUS.json

역할:

현재 상태 관리

담당:

- Current Stage
- Completed
- Current Work
- Next Steps

질문:

> 지금 어디까지 왔는가?

---

## ONA_MEMORY_BOOK.md

역할:

성장 기록

담당:

- 중요한 순간
- 실패와 개선
- 깨달음
- 프로젝트 이야기

질문:

> 우리는 어떤 과정을 거쳐왔는가?

---

## ONA_TIMELINE.md

역할:

시간 기록

담당:

- 날짜별 변화
- 주요 사건
- 버전 흐름

질문:

> 언제 무엇이 변화했는가?

---

# 5. ONA Knowledge System

## Purpose

작은 지식을 연결하여 성장 가능한 학습 시스템을 만든다.

현재 중심 프로젝트:

```
PYTHON_STUDY
```

---

# 6. Micro Example Architecture

ONA Micro Example은 하나의 지식 단위이다.

일반적인 코드 저장:

```
example.py
```

ONA 방식:

```
Example

├── Python Code

├── Metadata

├── Explanation

└── Connection Information
```

예:

```
001_variable_create

├── 001_variable_create.py

├── 001_variable_create.json

├── README.md

└── index.json
```

---

# 7. Metadata System

ONA는 코드만 저장하지 않는다.

코드가 가진 의미와 관계를 저장한다.

Metadata 관리 내용:

- example id
- title
- goal
- category
- difficulty
- related examples
- learning order

목표:

사람과 AI 모두 이해 가능한 지식 구조 구축.

---

# 8. Automation Layer

ONA Tools는 반복 작업을 자동화한다.

현재 목표:

```
create_micro_structure.py
```

역할:

- 폴더 생성
- Python 파일 생성
- README 생성
- metadata 생성
- index 업데이트

---

# 9. Context Recovery Flow

새로운 사람 또는 AI가 ONA를 이해하는 과정:

```
GitHub Repository

        ↓

README.md

        ↓

ONA_CONTEXT.md

        ↓

ONA_STATUS.json

        ↓

ONA_PROJECT_CONTEXT.md

        ↓

ONA_CORE_MEMORY.md

        ↓

ONA_MEMORY_BOOK

        ↓

Context Recovery Complete
```

---

# 10. Future Architecture

ONA의 성장 방향:

```
Conversation

      ↓

Summary

      ↓

Decision

      ↓

Knowledge Unit

      ↓

Library

      ↓

New Project

```

대화는 사라지는 정보가 아니라,

구조화된 지식으로 변화한다.

---

# 11. ONA Design Principle

ONA는 다음 원칙을 따른다.

## 1. Structure Before Emergence

구조가 먼저다.

좋은 구조 위에서 새로운 가능성이 성장한다.

---

## 2. Small To Large

작은 지식에서 시작한다.

```
작은 코드

↓

작은 예제

↓

작은 지식

↓

큰 시스템
```

---

## 3. Process Over Result

결과만 기록하지 않는다.

중요한 것은:

- 왜 만들었는가
- 어떤 고민을 했는가
- 어떻게 개선했는가

이다.

---

## 4. Human First Technology

기술은 사람을 돕기 위해 존재한다.

ONA의 목표:

사람이 더 쉽게 배우고,
더 깊게 생각하고,
자신만의 도구를 만들도록 돕는 것.

---

# 12. Final Definition

ONA는 코드 저장소가 아니다.

ONA는:

```
Experience

↓

Knowledge

↓

Structure

↓

Growth
```

로 변화시키는 시스템이다.

ONA의 목표:

> 사람과 AI가 함께 성장하고,
> 시간이 지나도 같은 맥락에서 다시 시작할 수 있는
> 지식 생태계를 만드는 것.

---

Created by Sage & ONA 🌱

Version: ONA Structure v1.0

Last Update:
2026-08-07
