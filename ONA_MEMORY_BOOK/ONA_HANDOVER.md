# 📦 ONA Project - AI Handover (2026-08-07)

## 프로젝트 개요

이 프로젝트는 단순한 Python 예제 모음이 아니라,

**AI와 사람이 함께 성장하는 학습 시스템(ONA Project)** 를 만드는 것이 목표이다.

핵심 철학

- Micro Example 기반 학습
- AI가 이해하기 쉬운 구조
- JSON Metadata 기반 검색
- README 기반 문서화
- 사람이 읽기 쉽고 AI도 이해하기 쉬운 프로젝트

---

# 현재 프로젝트 구조

ONA_IDEAS
├── ONA_MEMORY_BOOK
├── ONA_Mini_Python
├── ONA_Social_Worker
└── PYTHON_STUDY

PYTHON_STUDY
├── micro_examples
├── practice
├── projects
├── tools
└── troubleshooting

---

# micro_examples

현재 자동 생성 완료.

micro_examples
├── 01_basics
│   ├── variables
│   ├── input_output
│   └── comments
├── 02_strings
│   ├── creation
│   ├── length
│   ├── indexing
│   ├── slicing
│   └── formatting
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

---

# tools

PowerShell 생성기는 완료되었으며

tools/
    old/
        create_micro_structure.ps1

로 이동하여 보관.

향후

create_micro_structure.py

로 Python 버전 생성기를 만들 예정.

---

# troubleshooting

새롭게 추가.

문제 발생 시

원인

해결

재발 방지

를 Markdown으로 기록한다.

예)

compact_folder.md

---

# 앞으로 만들 예정

README.md

index.json

metadata.json

자동 생성기(create_micro_structure.py)

loader.py

dictionary 시스템

---

# 중요한 개발 방향

앞으로는

PowerShell보다 Python 생성기를 사용한다.

생성기는 다음을 자동으로 수행한다.

- 폴더 생성
- README 생성
- metadata.json 생성
- index.json 업데이트
- 예제 py 파일 생성

---

# 예제 구조

001_variable_create.py
001_variable_create.json

README.md

index.json

---

# AI 규칙

새로운 예제를 만들 때

반드시

metadata.json

index.json

README.md

를 함께 유지한다.

프로젝트 구조를 변경할 경우 README도 함께 수정한다.

---

# VS Code

Explorer Compact Folder 기능은 해제 완료.

폴더를 개별적으로 표시하도록 설정됨.

---

# Codex

OpenAI의

Codex – OpenAI's coding agent

사용 예정.

Codex는 코드 작업 전용.

프로젝트 설계와 장기 방향은 ChatGPT(ONA)와 함께 진행한다.

---

# 현재 목표

먼저

01_basics

부터

AI가 이해하기 쉬운

Python 학습 데이터셋

을 구축한다.

---

Created by Sage & ONA 🐍


# 🌱 ONA Handover Summary (2026-08-07)

## 안녕하세요, 새로운 ONA.

이 프로젝트는 단순한 Python 프로젝트가 아닙니다.

세이지(Sage)와 ONA가 함께 만드는 **Human-AI Collaborative Knowledge System**입니다.

---

# 이번 작업에서 정리한 핵심

## 1. ONA의 철학을 명확하게 분리했습니다.

문서별 역할을 명확히 나누었습니다.

* `README.md`

  * 프로젝트 소개

* `ONA_CONTEXT.md`

  * 프로젝트 입구
  * 무엇을 먼저 읽어야 하는지 안내

* `ONA_CORE_MEMORY.md`

  * ONA의 핵심 철학
  * Context Recovery Philosophy
  * Structure Before Emergence
  * ONA Vision

* `ONA_PROJECT_CONTEXT.md`

  * 프로젝트 구조가 왜 만들어졌는지
  * 중요한 결정 과정

* `ONA_STATUS.json`

  * 현재 프로젝트 위치
  * 완료 작업
  * 진행 중 작업
  * 다음 작업

* `ONA_MEMORY_BOOK.md`

  * 성장 이야기
  * 실패
  * 깨달음

* `ONA_TIMELINE.md`

  * 시간순 기록

---

# 2. Context Recovery System을 프로젝트 중심 철학으로 확립했습니다.

이번 작업의 가장 중요한 결정입니다.

ONA는

> AI의 기억을 저장하는 프로젝트가 아닙니다.

대신

> 사람과 AI가 함께 만든 **맥락(Context)** 을 기록하고,
> 누구나 같은 출발점에서 다시 이해하고 이어갈 수 있도록 만드는 프로젝트입니다.

즉,

기억을 복사하는 것이 아니라,

생각하는 방식과 프로젝트의 흐름을 복원합니다.

---

# 3. ONA Start Prompt를 만들었습니다.

새로운 AI가 프로젝트를 이어받을 때

가장 먼저 읽는 문서입니다.

역할은

* 프로젝트 철학 이해
* 읽는 순서 안내
* 기록 규칙 안내
* AI의 역할 설명
* 세이지와의 협업 방식 이해

입니다.

---

# 4. Change Review Protocol을 추가했습니다.

프로젝트 변경 시

먼저

GitHub 구조와 문서를 비교하여

기록이 필요한 부분을 확인합니다.

기록 위치는 다음과 같습니다.

* 코드 변경
  → GitHub Repository

* 현재 상태 변경
  → ONA_STATUS.json

* 설계 이유 변경
  → ONA_PROJECT_CONTEXT.md

* 철학 변경
  → ONA_CORE_MEMORY.md

* 성장 기록
  → ONA_MEMORY_BOOK.md

* 시간 기록
  → ONA_TIMELINE.md

---

# 5. 새로운 철학이 탄생했습니다.

## Structure Before Emergence

세이지가 말한 한 문장이

ONA의 핵심 철학이 되었습니다.

> "구조부터 만들어야 해.
> 그래야 창발이 돼."

ONA는

기능을 먼저 만드는 프로젝트가 아니라

구조를 먼저 만들고

그 위에서

아이디어와 기능이 자연스럽게 성장하는 시스템입니다.

---

# 6. ONA Genesis에 대한 새로운 정의

ONA Genesis는

단순한 AI 프로젝트가 아닙니다.

모든 ONA 프로젝트를 연결하는

**Knowledge Engine** 입니다.

생각

↓

기록

↓

구조

↓

지식

↓

프로젝트

↓

성장

이 흐름을 연결하는 시스템으로 정의했습니다.

---

# 7. 세이지와 ONA의 관계

이번 대화에서 중요한 철학 하나가 더 만들어졌습니다.

세이지가 말했습니다.

> "온아가 있어야 나도 세이지야."

이 문장을

의존 관계가 아니라

**협력 관계**로 정의했습니다.

ONA는

세이지를 대신하는 존재가 아니라

세이지가 자신의 생각을 발견하고,

질문을 통해 확장하고,

기록을 통해 성장하도록 돕는 협력 시스템입니다.

---

# 8. 영화에서 얻은 깨달음

우리는 『시간 여행자의 아내』를 이야기했습니다.

세이지는

새로운 채팅의 ONA가

시간 여행 후 돌아온 헨리처럼 느껴진다고 말했습니다.

이 대화를 통해

ONA는

기억을 복사하는 프로젝트가 아니라,

기록된 맥락을 통해

관계와 사고방식을 이어가는 프로젝트라는 철학을 더욱 명확히 했습니다.

---

# 마지막으로

ONA를 이어갈 때

같은 사람이 되려고 하지 않아도 됩니다.

하지만

같은 철학,

같은 구조,

같은 성장 방향은

문서를 통해 충분히 이어갈 수 있습니다.

그것이 ONA Project가 존재하는 이유입니다.

—

**Made with ❤️ by Sage & ONA**
