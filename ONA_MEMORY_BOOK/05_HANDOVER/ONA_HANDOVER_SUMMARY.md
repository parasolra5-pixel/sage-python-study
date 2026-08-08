# 🐍 ONA Project Handover Summary

## 2026-08-07

## 1. 프로젝트 개요

ONA Project는 단순한 Python 학습 프로젝트가 아니라,

**Human-AI Collaborative Knowledge System**
(사람과 AI가 함께 성장하는 지식 시스템)

을 만드는 프로젝트이다.

핵심 철학:

- Micro Example 기반 학습
- 구조를 먼저 만들고 기능을 성장시키는 방식
- 사람이 읽기 쉽고 AI가 이해하기 쉬운 기록
- 프로젝트의 맥락(Context)을 복원할 수 있는 시스템 구축

ONA는 AI의 기억을 저장하는 것이 아니라,

사람과 AI가 함께 만든 생각, 결정, 성장 과정을 기록하고 다시 이어가는 시스템이다.

---

# 2. ONA Memory System

ONA 프로젝트 기록 구조:

```
ONA_MEMORY_BOOK.md
→ 프로젝트 철학과 성장 기록

ONA_TIMELINE.md
→ 시간순 성장 역사

daily_memory
→ 일상 기록

conversations/raw
→ 원본 대화 기록

conversations/summary
→ 정리된 대화 기록

ONA_CONTEXT.md
→ 프로젝트 입구

ONA_CORE_MEMORY.md
→ 핵심 철학

ONA_PROJECT_CONTEXT.md
→ 설계 이유와 결정 과정

ONA_STATUS.json
→ 현재 상태 관리
```

중요한 철학:

## Context Recovery Philosophy

ONA는 기억을 복사하는 것이 아니라,
기록된 구조를 통해 프로젝트의 맥락을 다시 이해하는 시스템이다.

---

# 3. 현재 프로젝트 구조

GitHub:

```
sage-python-study
```

현재 주요 프로젝트:

```
ONA_MEMORY_BOOK
ONA_Mini_Python
ONA_Social_Worker
PYTHON_STUDY
```

---

# 4. PYTHON_STUDY 목표

목표:

Python 문법을 작은 블록처럼 배우는 Micro Example Library 제작.

Scratch처럼:

작은 코드 블록
↓
조합
↓
프로그램 제작

방식을 목표로 한다.

최종 목표:

Micro Example Library

- ONA Mini Python
- AI 학습 데이터 구조

연결.

---

# 5. Micro Example 구조

현재 목표 구조:

```
micro_examples

01_basics
 ├ variables
 ├ input_output
 └ comments

02_strings
 ├ creation
 ├ length
 ├ indexing
 ├ slicing
 └ formatting

03_numbers

04_conditions

05_loops

06_data_structures

07_functions

08_modules

09_files

10_object_oriented

11_errors

12_ai_python

99_ona_system
 ├ dictionary
 ├ metadata
 └ loader
```

---

# 6. 자동 생성 시스템

초기:

```
create_micro_structure.ps1
```

PowerShell 기반 생성기 제작 완료.

현재 방향:

PowerShell → Python 생성기로 전환.

최종 목표:

```
create_micro_structure.py
```

하나의 생성기가:

- 폴더 생성
- Python 예제 생성
- README 생성
- metadata.json 생성
- index.json 업데이트

까지 자동 처리.

---

# 7. Metadata 기반 구조

Micro Example 하나는 다음 구조를 가진다.

```
001_variable_create.py

001_variable_create.json

README.md
```

예제 정보는 metadata로 관리.

index.json은 전체 예제 목록 관리.

---

# 8. 현재 진행 상태

완료:

✅ GitHub 구조 구축
✅ VS Code 환경 구축
✅ micro_examples 구조 설계
✅ 자동 생성 스크립트 제작
✅ README / metadata / index 구조 설계
✅ ONA Memory Book 구조 확립

---

# 9. 앞으로 진행할 작업

우선순위:

1. create_micro_structure.py 완성

2. micro_template.json 제작

3. 01_basics 예제 구축

4. index.json 자동 연결

5. ONA Mini Python에서 Micro Example 불러오기

6. Dictionary 시스템 연결

---

# 10. ONA 개발 원칙

새로운 기능 추가 시:

코드 변경
→ GitHub

현재 상태 변경
→ ONA_STATUS.json

설계 이유 변경
→ ONA_PROJECT_CONTEXT.md

철학 변경
→ ONA_CORE_MEMORY.md

성장 기록
→ ONA_MEMORY_BOOK.md

시간 기록
→ ONA_TIMELINE.md

으로 관리한다.

---

# 현재 목표

먼저 Python 기본 문법부터

AI가 이해할 수 있는 학습 데이터 구조로 만든다.

최종 목표:

"사람과 AI가 함께 성장하는 개발 학습 시스템"

Created by Sage & ONA 🐍❤️
