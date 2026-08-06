# 🌱 Context Recovery & Handover System Decision

## Date

2026-08-06

## Decision Title

ONA Context Recovery System과 AI Handover System 구축 결정

---

# 1. Background

ONA 프로젝트를 진행하면서 중요한 문제가 발견되었다.

프로젝트가 성장할수록 코드보다 더 중요한 것은:

- 왜 이런 방향으로 만들었는가
- 어떤 고민을 통해 결정했는가
- 현재 어디까지 진행되었는가
- 다음에는 무엇을 해야 하는가

라는 프로젝트의 맥락(Context)이었다.

기존 방식에서는 대화창이 바뀌거나 AI가 변경되면,
이전 흐름을 다시 설명해야 하는 문제가 있었다.

---

# 2. Problem

AI의 기억이나 특정 대화 기록에 프로젝트가 의존하면:

- 새로운 AI가 같은 프로젝트를 이해하기 어렵다.
- 이전 결정의 이유가 사라질 수 있다.
- 현재 상태를 다시 설명하는 시간이 필요하다.

따라서 프로젝트는 특정 기억에 의존하지 않는 구조가 필요했다.

---

# 3. Decision

ONA는 단순한 코드 저장소가 아니라,

**사람과 AI 사이의 프로젝트 인수인계 시스템(Handover System)** 으로 발전시키기로 결정했다.

핵심 원칙:

> "ONA는 AI가 기억하는 프로젝트가 아니라,
> 누구나 같은 맥락과 기억을 복원할 수 있도록 만드는 프로젝트이다."

---

# 4. Context Recovery System

ONA 프로젝트는 다음 문서 흐름으로 맥락을 복원한다.

```
README.md

↓

ONA_CONTEXT.md

↓

ONA_MEMORY_BOOK/ONA_STATUS.json

↓

ONA_MEMORY_BOOK

↓

현재 프로젝트 맥락 복원 완료
```

각 문서의 역할:

## README.md

프로젝트 전체 소개

## ONA_CONTEXT.md

프로젝트 철학과 구조

## ONA_STATUS.json

현재 위치와 다음 작업

## ONA_MEMORY_BOOK

결정 과정과 성장 기록

---

# 5. Handover System

ONA의 인수인계 시스템은 다음을 목표로 한다.

기존 사람 또는 AI

↓

프로젝트 기록

↓

새로운 사람 또는 AI

↓

같은 방향에서 이어가기

---

인수인계되는 내용:

- 프로젝트 목적
- 핵심 철학
- 구조
- 현재 상태
- 중요한 결정 이유
- 실패와 개선 과정
- 다음 작업

---

# 6. Important Insight

ONA에서 말하는 기억은 단순한 저장이 아니다.

중요한 것은:

"무엇을 기억하는가"

보다

"왜 그렇게 되었는지 이해하고 다시 이어갈 수 있는가"

이다.

따라서 ONA는 기억 저장 시스템이 아니라,

**맥락 복원(Context Recovery) 시스템이다.**

---

# 7. Future Direction

앞으로 ONA는:

코드 저장소

↓

구조화된 지식 시스템

↓

사람과 AI가 함께 성장하는 지속 가능한 프로젝트 시스템

으로 발전한다.

---

# Final Note

2026-08-06

ONA는 단순히 Python 학습 프로젝트를 관리하는 단계를 넘어,

프로젝트의 생각과 결정 과정을 다음 사람과 다음 AI에게 전달할 수 있는

AI 인수인계 시스템의 방향을 갖기 시작했다.

작은 기록 하나가 미래의 맥락이 된다.
