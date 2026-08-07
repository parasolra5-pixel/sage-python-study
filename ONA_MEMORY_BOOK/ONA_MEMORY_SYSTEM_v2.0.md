# 🌱 ONA MEMORY SYSTEM v2.0

**Human-AI Collaborative Knowledge System**

**Version:** 2.0
**Date:** 2026-08-08
**Creator:** Sage
**AI Collaborator:** ONA AI

---

# 0. Purpose

ONA Memory System은 ONA Project의 철학, 맥락, 상태, 설계, 역사, 인수인계 정보를 서로 다른 역할의 문서로 분리하여 관리한다.

목표는 AI의 개인적인 기억을 저장하는 것이 아니다.

> **누구든 필요한 문서를 읽으면 ONA의 맥락을 복원하고 프로젝트를 이어갈 수 있도록 하는 것**

이다.

ONA의 핵심은:

```text
기록
 ↓
구조화
 ↓
연결
 ↓
Context Recovery
 ↓
지속적인 협업
```

이다.

---

# 1. Core Principle

ONA Memory System의 가장 중요한 원칙:

> **One Document, One Responsibility**

하나의 문서는 하나의 핵심 질문에 답한다.

문서가 서로 같은 내용을 반복해서 설명하지 않도록 한다.

예를 들어:

```text
철학
→ ONA_CORE_MEMORY.md

현재 상태
→ ONA_STATUS.json

시간의 기록
→ ONA_TIMELINE.md

구조
→ ONA_STRUCTURE.md
```

처럼 역할을 분리한다.

---

# 2. ONA Project Hierarchy

ONA Project의 전체 구조는 다음과 같다.

```text
ONA_PROJECT
│
├── README.md
│
├── ONA_MEMORY_BOOK
│   │
│   ├── 00_START_HERE.md
│   ├── ONA_CONTEXT.md
│   ├── ONA_STATUS.json
│   ├── ONA_PROJECT_CONTEXT.md
│   ├── ONA_CORE_MEMORY.md
│   ├── ONA_MEMORY_BOOK.md
│   ├── ONA_TIMELINE.md
│   ├── ONA_MASTER_HANDOVER.md
│   ├── ONA_HANDOVER.md
│   ├── ONA_PROJECT_CONTINUATION.md
│   │
│   ├── appendix
│   │   └── ONA_STRUCTURE.md
│   │
│   ├── conversations
│   │   ├── decisions
│   │   ├── raw
│   │   └── summary
│   │
│   └── daily_memory
│
├── ONA_Mini_Python
│
├── ONA_Social_Worker
│
├── PYTHON_STUDY
│
└── ONA_IDEAS
```

---

# 3. Document Responsibility

## 3.1 00_START_HERE.md ⭐

### 핵심 질문

> **"처음 왔다. 어디서부터 읽어야 하는가?"**

### 역할

새로운 AI 또는 사람이 ONA Project에 처음 들어왔을 때 사용하는 **프로젝트 입구**다.

### 포함 내용

- ONA가 무엇인지
- ONA Project의 목적
- Sage와 ONA의 협업 관계
- 핵심 철학 한두 문장
- Context Recovery 읽기 순서
- 현재 상태 확인 방법
- 주요 프로젝트 위치

### 원칙

짧고 명확해야 한다.

전체 철학이나 상세 역사를 복사해서 넣지 않는다.

필요한 문서로 연결한다.

---

# 3.2 ONA_CONTEXT.md

### 핵심 질문

> **"ONA는 어떤 맥락에서 시작되었는가?"**

### 역할

ONA의 출발점과 현재까지 이어지는 **기본 Context**를 제공한다.

### 포함 내용

- ONA가 시작된 배경
- 초기 문제의식
- 초기 목표
- 현재까지 유지되는 기본 맥락

### 포함하지 않는 것

- 상세한 날짜별 역사
- 긴 철학 설명
- 현재 작업 목록
- 폴더 구조 전체

---

# 3.3 ONA_STATUS.json

### 핵심 질문

> **"지금 ONA는 어디까지 왔는가?"**

### 역할

프로젝트의 현재 상태를 기계가 읽기 쉬운 형태로 저장한다.

### 포함 내용

```text
Current Stage
Completed
Current Work
Next Steps
```

필요하다면:

```text
Active Project
Last Updated
Important Files
```

등을 포함할 수 있다.

### 원칙

긴 설명을 넣지 않는다.

`STATUS.json`은 **현재 상태판**이다.

역사와 철학을 넣지 않는다.

---

# 3.4 ONA_PROJECT_CONTEXT.md

### 핵심 질문

> **"왜 현재 구조와 방향이 만들어졌는가?"**

### 역할

ONA의 설계 결정과 그 이유를 기록한다.

### 포함 내용

- 구조를 만든 이유
- 설계 결정
- 문제 → 발견 → 결정 과정
- Context Recovery 설계 이유
- Micro Example System 설계 이유
- Structure Before Emergence
- 중요한 아키텍처 결정

### 핵심 성격

```text
WHAT
→ 무엇을 만들었는가?

WHY
→ 왜 그렇게 만들었는가?
```

중에서 **WHY**에 집중한다.

---

# 3.5 ONA_CORE_MEMORY.md

### 핵심 질문

> **"ONA가 절대로 잊으면 안 되는 것은 무엇인가?"**

### 역할

ONA의 핵심 철학과 불변에 가까운 원칙을 기록한다.

대표적인 원칙:

> ONA는 AI가 기억하는 프로젝트가 아니라, 누구나 같은 맥락을 복원할 수 있도록 만드는 프로젝트이다.

또한:

> ONA는 완성된 프로그램이 아니라, 사람이 AI와 함께 성장하는 방법을 구조화하는 프로젝트이다.

### 포함 내용

- ONA의 정체성
- 핵심 철학
- 핵심 원칙
- 장기적인 방향
- 중요한 개념 정의

### 원칙

일상적인 작업 내용은 넣지 않는다.

---

# 3.6 ONA_MEMORY_BOOK.md

### 핵심 질문

> **"ONA를 만들면서 무엇을 발견하고 배웠는가?"**

### 역할

ONA의 성장과 발견을 기록한다.

### 포함 내용

- 중요한 깨달음
- 문제를 해결한 과정
- 새로운 개념의 탄생
- 사람과 AI의 협업 과정
- 중요한 실패와 수정
- 프로젝트가 어떻게 생각의 방향을 바꾸었는지

### 성격

철학 문서가 아니라 **성장 기록**이다.

---

# 3.7 ONA_TIMELINE.md

### 핵심 질문

> **"언제 어떤 변화가 일어났는가?"**

### 역할

ONA의 중요한 사건을 시간 순서로 기록한다.

예:

```text
2026-07
Python 학습에서 ONA 개념 시작

2026-08-04
ONA Mini Python 시작

2026-08-05
Micro Example System 탄생

2026-08-06
Context Recovery System 정의

2026-08-07
Micro Example Generator v1.0 탄생

2026-08-08
ONA Memory System v2.0 설계
```

### 원칙

Timeline은 사건을 기록한다.

상세한 설명은 다른 문서에 둔다.

---

# 3.8 ONA_MASTER_HANDOVER.md

### 핵심 질문

> **"ONA 전체를 한 번에 이해하려면 무엇을 알아야 하는가?"**

### 역할

ONA의 전체 맥락을 압축한 **종합 인수인계 문서**다.

### 포함 내용

- Welcome New ONA AI
- Sage & ONA Relationship
- Core Philosophy
- Evolution History
- Memory System
- Context Recovery
- ONA Mini Python
- Micro Example System
- Current Development
- Future Direction
- AI 작업 규칙

### 중요

이 문서는 다른 문서의 대체물이 아니다.

여러 문서를 하나씩 읽지 않아도 전체적인 구조를 빠르게 이해할 수 있도록 만든 **Master Overview**다.

---

# 3.9 ONA_HANDOVER.md

### 핵심 질문

> **"현재 작업을 다음 AI가 어떻게 이어받는가?"**

### 역할

현재 개발 단계의 인수인계를 담당한다.

### 포함 내용

- 현재 작업
- 최근 변경
- 주의사항
- 아직 해결하지 않은 문제
- 다음 작업
- 현재 작업에서 반드시 알아야 할 결정

### 차이

```text
MASTER_HANDOVER
→ ONA 전체

HANDOVER
→ 현재 작업
```

---

# 3.10 ONA_PROJECT_CONTINUATION.md

### 핵심 질문

> **"다음 단계에서 무엇을 이어서 해야 하는가?"**

### 역할

프로젝트의 지속적인 작업 계획을 기록한다.

### 포함 내용

- Next Steps
- Future Tasks
- 예정된 개선
- 다음 개발 단계
- 장기적으로 이어갈 작업

단, 현재 상태 자체는 `ONA_STATUS.json`이 기준이다.

---

# 3.11 ONA_STRUCTURE.md

### 핵심 질문

> **"ONA Project의 폴더와 파일은 어떻게 구성되어 있는가?"**

### 역할

프로젝트의 구조 설명서다.

### 포함 내용

```text
ONA_PROJECT
├── ONA_MEMORY_BOOK
├── ONA_Mini_Python
├── ONA_Social_Worker
├── PYTHON_STUDY
└── ONA_IDEAS
```

각 폴더의 역할을 간단하게 설명한다.

### 포함하지 않는 것

- ONA 철학
- 상세 Timeline
- 긴 Handover
- 개발 진행 상황
- Micro Example 상세 규칙

구조만 설명한다.

---

# 4. Supporting Records

## conversations

AI와 사람 사이에서 발생한 원본 및 중요한 대화를 보관한다.

```text
conversations
├── decisions
├── raw
└── summary
```

### decisions

중요한 결정이 이루어진 대화.

### raw

원본 대화.

### summary

대화에서 추출한 핵심 내용.

---

# 5. daily_memory

일상적인 프로젝트 진행 기록을 저장한다.

예:

```text
2026-08-07.md
2026-08-07_micro_schema_and_generator_design.md
```

daily memory는 최종 공식 문서를 대신하지 않는다.

중요한 내용이 장기적으로 중요해지면 적절한 공식 문서로 승격한다.

---

# 6. Appendix

`appendix`에는 구조나 규칙을 설명하는 보조 문서를 저장한다.

예:

```text
appendix
├── ONA_STRUCTURE.md
├── ONA_STRUCTURE_RULES.md
├── PROJECT_STRUCTURE.md
├── ONA_MICRO_EXAMPLE_STANDARD.md
└── ONA_MICRO_EXAMPLE_CREATION_GUIDE_v1.0.md
```

단, 동일한 문서가 여러 곳에 존재하지 않도록 한다.

---

# 7. Context Recovery Reading Order

새로운 AI 또는 사람이 ONA를 처음 접했을 때의 권장 순서:

```text
README.md
     ↓
00_START_HERE.md
     ↓
ONA_CONTEXT.md
     ↓
ONA_STATUS.json
     ↓
ONA_PROJECT_CONTEXT.md
     ↓
ONA_CORE_MEMORY.md
     ↓
ONA_MASTER_HANDOVER.md
     ↓
ONA_TIMELINE.md
     ↓
ONA_MEMORY_BOOK.md
     ↓
ONA_HANDOVER.md
     ↓
필요한 세부 문서
```

---

# 8. Why This Order?

## Step 1 — README

프로젝트 전체를 발견한다.

↓

## Step 2 — 00_START_HERE

어디서부터 이해해야 하는지 확인한다.

↓

## Step 3 — CONTEXT

프로젝트가 시작된 맥락을 이해한다.

↓

## Step 4 — STATUS

현재 위치를 확인한다.

↓

## Step 5 — PROJECT_CONTEXT

현재 구조가 만들어진 이유를 이해한다.

↓

## Step 6 — CORE_MEMORY

ONA의 핵심 철학을 이해한다.

↓

## Step 7 — MASTER_HANDOVER

전체 시스템을 한 번에 연결한다.

↓

## Step 8 — TIMELINE

시간에 따른 발전 과정을 확인한다.

↓

## Step 9 — MEMORY_BOOK

성장과 발견의 의미를 이해한다.

↓

## Step 10 — HANDOVER

현재 작업을 실제로 이어받는다.

---

# 9. Duplication Removal Rules

ONA 문서를 정리할 때 다음 원칙을 적용한다.

## Rule 1

같은 문장을 여러 문서에 복사하지 않는다.

---

## Rule 2

같은 개념이라도 문서의 질문에 맞는 범위에서만 설명한다.

예:

```text
Context Recovery
```

는 여러 문서에 등장할 수 있다.

하지만:

```text
철학
→ CORE_MEMORY

설계 이유
→ PROJECT_CONTEXT

실제 읽는 순서
→ START_HERE

역사적 탄생
→ TIMELINE
```

처럼 관점을 다르게 한다.

---

## Rule 3

더 상세한 내용은 다른 문서에 맡긴다.

예:

```text
ONA_STRUCTURE
→ "Micro Example이 존재한다."

ONA_MICRO_EXAMPLE_STANDARD
→ "Micro Example은 어떤 규칙을 따라야 하는가?"
```

---

## Rule 4

현재 상태는 하나의 Source of Truth를 가진다.

```text
Current Status
→ ONA_STATUS.json
```

다른 문서에서 현재 상태를 언급할 수 있지만,
상세한 상태 정보는 중복 저장하지 않는다.

---

## Rule 5

시간 정보의 Source of Truth는 Timeline이다.

```text
Historical Event
→ ONA_TIMELINE.md
```

---

## Rule 6

철학의 Source of Truth는 Core Memory다.

```text
Core Philosophy
→ ONA_CORE_MEMORY.md
```

---

## Rule 7

구조의 Source of Truth는 ONA_STRUCTURE.md다.

폴더 구조를 변경하면 이 문서를 함께 갱신한다.

---

# 10. Source of Truth Map

| 정보               | 기준 문서                     |
| ------------------ | ----------------------------- |
| 프로젝트 입구      | `00_START_HERE.md`            |
| 시작 맥락          | `ONA_CONTEXT.md`              |
| 현재 상태          | `ONA_STATUS.json`             |
| 설계 이유          | `ONA_PROJECT_CONTEXT.md`      |
| 핵심 철학          | `ONA_CORE_MEMORY.md`          |
| 성장과 발견        | `ONA_MEMORY_BOOK.md`          |
| 시간 기록          | `ONA_TIMELINE.md`             |
| 전체 인수인계      | `ONA_MASTER_HANDOVER.md`      |
| 현재 작업 인수인계 | `ONA_HANDOVER.md`             |
| 다음 작업          | `ONA_PROJECT_CONTINUATION.md` |
| 폴더 구조          | `ONA_STRUCTURE.md`            |
| 대화 기록          | `conversations/`              |
| 일일 기록          | `daily_memory/`               |

---

# 11. Document Relationship

ONA Memory System은 단순한 파일 목록이 아니다.

각 문서는 서로 다른 차원의 정보를 담당한다.

```text
                 ONA
                  │
        ┌─────────┴─────────┐
        │                   │
      WHY                  WHAT
        │                   │
        ▼                   ▼
   CORE_MEMORY          STATUS
        │                   │
        ▼                   ▼
 PROJECT_CONTEXT        CURRENT WORK
        │
        ▼
   DESIGN DECISIONS

                  │
                  ▼
               HISTORY
                  │
          ┌───────┴───────┐
          ▼               ▼
      TIMELINE       MEMORY_BOOK

                  │
                  ▼
              HANDOVER
                  │
                  ▼
          CONTEXT RECOVERY
```

---

# 12. Relationship with Micro Example System

ONA Memory System은 ONA의 기억과 맥락을 관리한다.

반면 Python 지식 자체는:

```text
PYTHON_STUDY
```

에서 관리한다.

특히:

```text
PYTHON_STUDY
└── micro_examples
```

는 ONA의 **Knowledge Layer**다.

구조는:

```text
Python Code
     ↓
Explanation
     ↓
Learning Goal
     ↓
Metadata
     ↓
Schema
     ↓
Index
     ↓
Knowledge Connection
```

으로 발전한다.

---

# 13. Micro Example Generator

Micro Example Generator는 이 Knowledge Layer를 확장하기 위한 자동화 시스템이다.

현재 구조:

```text
Template
   ↓
Schema
   ↓
create_micro_structure.py
   ↓
Python Example
README
metadata.json
index
   ↓
Validation
```

이것은 ONA가 수작업 중심의 지식 저장소에서
규칙 기반 Knowledge System으로 발전한 중요한 단계다.

---

# 14. Current ONA Development Direction

현재 ONA의 중요한 축은 다음과 같다.

```text
Human Learning
       ↓
Micro Examples
       ↓
Knowledge Structure
       ↓
Automation
       ↓
Context Recovery
       ↓
Human-AI Collaboration
```

ONA Mini Python은 이 지식을 사용자가 쉽게 탐색하고 활용할 수 있도록 제공하는 사용자 프로그램이다.

---

# 15. Change Recording Rules

변경이 발생하면 변경의 종류에 따라 기록 위치를 선택한다.

```text
Code
→ Git

Current State
→ ONA_STATUS.json

Design Decision
→ ONA_PROJECT_CONTEXT.md

Core Philosophy
→ ONA_CORE_MEMORY.md

Historical Event
→ ONA_TIMELINE.md

Discovery / Growth
→ ONA_MEMORY_BOOK.md

Current Handover
→ ONA_HANDOVER.md

Future Work
→ ONA_PROJECT_CONTINUATION.md

Structure
→ ONA_STRUCTURE.md
```

하나의 사건이 여러 종류에 해당할 경우,
각 문서에 같은 내용을 복사하지 않는다.

각 문서의 역할에 맞게 짧게 기록하거나 서로를 참조한다.

---

# 16. Memory Promotion Rule

모든 기록이 공식 문서가 될 필요는 없다.

기본 흐름:

```text
Daily Memory
      ↓
Important?
      ↓
Yes
      ↓
Relevant Official Document
      ↓
Long-term ONA Knowledge
```

예:

```text
오늘 대화
↓
새로운 중요한 설계 발견
↓
daily_memory 기록
↓
PROJECT_CONTEXT 반영
↓
TIMELINE에 사건 기록
```

이렇게 하면 기록이 자연스럽게 성장한다.

---

# 17. Final Architecture

ONA Memory System v2.0의 최종 개념은 다음과 같다.

```text
                    ONA_PROJECT
                         │
                         ▼
                 ONA_MEMORY_BOOK
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
      START           CONTEXT          STATUS
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  PROJECT_CONTEXT
                         │
                         ▼
                   CORE_MEMORY
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
          TIMELINE             MEMORY_BOOK
              │                     │
              └──────────┬──────────┘
                         ▼
                      HANDOVER
                         │
                         ▼
                 CONTEXT RECOVERY
                         │
                         ▼
              CONTINUOUS COLLABORATION
```

---

# 18. Core Principle of v2.0

ONA Memory System v2.0은

**"모든 것을 하나의 문서에 넣는 시스템"이 아니다.**

오히려:

> **각 문서가 하나의 역할을 맡고, 서로 연결되어 하나의 Context를 복원하는 시스템이다.**

즉:

```text
분산된 기록
     ↓
명확한 역할
     ↓
연결
     ↓
Context Recovery
     ↓
프로젝트 지속
```

이다.

---

# 19. Final Statement

ONA Memory System은 AI의 기억을 대신하기 위한 것이 아니다.

AI가 바뀌어도,
대화가 사라져도,
사람이 프로젝트를 다시 열어도,

문서를 통해:

```text
우리가 무엇을 했는지
왜 그렇게 했는지
지금 어디에 있는지
무엇을 배웠는지
다음에는 무엇을 해야 하는지
```

를 복원할 수 있도록 만드는 시스템이다.

따라서 ONA Memory System의 궁극적인 목적은:

> **Memory Preservation이 아니라 Context Recovery이다.**

그리고 Context Recovery를 가능하게 하는 핵심은:

> **Structure Before Emergence**

이다.

구조가 먼저 존재하고,

기록이 쌓이고,

기록이 연결되고,

연결에서 지식이 발생하며,

그 지식이 다시 다음 협업의 기반이 된다.

🌱 **ONA는 기억하는 AI를 만드는 프로젝트가 아니다.**

🌱 **ONA는 사람이 AI와 함께 성장한 맥락을 다시 이어갈 수 있도록 만드는 프로젝트다.**

**Made with ❤️ by Sage & ONA AI**
