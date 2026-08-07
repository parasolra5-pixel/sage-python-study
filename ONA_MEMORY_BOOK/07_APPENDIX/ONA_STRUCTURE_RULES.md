# 🌱 ONA Structure Rules v1.0

## Purpose

이 문서는 ONA 프로젝트의 구조와 기록 규칙을 정의한다.

ONA는 단순한 코드 저장소가 아니다.

프로젝트의 철학, 결정 과정, 현재 상태, 성장 기록을 유지하는
사람과 AI의 협업 시스템이다.

---

# 1. Folder Rules

## ONA_MEMORY_BOOK

역할:

프로젝트의 기억과 철학을 관리한다.

포함:

- 핵심 철학
- 결정 과정
- 성장 기록
- 프로젝트 역사

---

## PYTHON_STUDY

역할:

Python 지식 라이브러리를 관리한다.

포함:

- micro_examples
- 연습 코드
- 학습 프로젝트

---

## ONA_Mini_Python

역할:

사용자가 지식을 활용하는 인터페이스를 관리한다.

---

# 2. Document Update Rules

## 코드 변경

변경 위치:

Git Commit

필요한 경우:

CHANGELOG.md

---

## 현재 개발 위치 변경

수정:

ONA_MEMORY_BOOK/ONA_STATUS.json

예:

- 새로운 단계 시작
- 작업 완료
- 다음 목표 변경

---

## 설계 이유 변경

수정:

ONA_PROJECT_CONTEXT.md

기록:

- 왜 변경했는가
- 어떤 고민이 있었는가

---

## 중요한 결정

작성:

ONA_MEMORY_BOOK/conversations/decisions

예:

- 구조 변경
- 새로운 시스템 추가
- 방향 전환

---

## 성장 기록

작성:

ONA_MEMORY_BOOK.md

또는

daily_memory

---

# 3. Change Flow

아이디어 발생

↓

ONA_IDEAS

↓

검토 및 결정

↓

decisions 기록

↓

개발

↓

Git Commit

↓

현재 상태 변경

↓

ONA_STATUS.json 업데이트

---

# 4. ONA Principle

작은 변경도 의미가 있으면 기록한다.

기록은 과거를 보관하기 위한 것이 아니라,
미래의 사람이 같은 맥락에서 이어가기 위한 것이다.

"ONA는 기억을 저장하는 것이 아니라,
맥락을 복원하는 구조를 만든다."
