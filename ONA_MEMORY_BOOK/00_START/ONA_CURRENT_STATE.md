# 🌱 ONA CURRENT STATE

> ONA Project와 ONA Mini Python의 현재 작업 위치를 기록하는 파일이다.
> 새 대화의 ONA AI는 이 파일을 먼저 확인하여 이전 작업의 맥락을 복구한다.

---

## 현재 프로젝트

**Project:** ONA — Human-AI Collaborative Knowledge System

**Active Area:** ONA Mini Python

ONA의 핵심 방향은 AI의 개인적 기억을 저장하는 것이 아니라,
구조화된 기록을 통해 사람과 AI의 공동 작업 맥락(Context)을 복구하고
지속적으로 발전시키는 것이다.

핵심 질문:

> 어떤 구조가 사람과 AI의 지속적인 협업을 실제로 더 지능적으로 만드는가?

---

## 현재 작업 위치

현재 `03_numbers/operators` Micro Example이 완료된 상태이다.

구조:

```text
PYTHON_STUDY/
└─ micro_examples/
   └─ 03_numbers/
      ├─ integer/
      ├─ float/
      └─ operators/
         ├─ 001_basic_operators.py
         ├─ README.md
         └─ metadata.json
```

---

## 마지막 완료 작업

### 03_numbers/operators

완료:

- `001_basic_operators.py`
- `README.md`
- `metadata.json`
- `micro_examples/index.json` 업데이트
- `tools/loader.py` 개선
- Category가 다른 동일 Topic을 Loader가 구분하도록 개선

정상 확인:

```text
python loader.py 03_numbers/operators
```

정상적으로 Topic 정보를 출력했다.

Git checkpoint:

```text
b386677 operators
```

---

## 현재 상태

`operators`는 완료된 checkpoint이다.

현재 다음 단계는 새로운 예제를 바로 만드는 것이 아니라,

> **03_numbers 전체 구조와 확장성을 검토하는 것**

이다.

검토 대상:

1. `integer`
2. `float`
3. `operators`
4. `index.json`
5. 각 Topic의 `metadata.json`
6. `loader.py`
7. Micro Example 생성 구조

---

## 다음 작업

다음 순서로 진행한다.

1. `03_numbers` 현재 구조 확인
2. `integer / float / operators`의 관계 확인
3. 현재 metadata 구조 검토
4. `index.json` 확장성 검토
5. `loader.py` 확장성 검토
6. 필요한 구조 개선이 있는지 판단
7. 구조가 안정되면 다음 Micro Example 결정
8. 테스트
9. ONA 기록
10. Git commit
11. Git push

---

## 작업 원칙

ONA Mini Python 작업은 다음 흐름을 따른다.

```text
작업
 ↓
테스트
 ↓
성공 확인
 ↓
기록할 가치 판단
 ↓
ONA 기록
 ↓
Git commit
 ↓
Git push
 ↓
다음 작업
```

중요한 구조적 변화가 있으면 세이지가 별도로 요청하지 않아도
ONA AI가 기록 필요성을 먼저 판단한다.

---

## 기록 완료 알림 원칙

ONA AI가 프로젝트의 현재 상태나 성장 과정에 기록할 가치가 있는 변화를 기록하면,
**반드시 세이지에게 기록 사실을 알려준다.**

알림에는 가능한 한 다음 내용을 포함한다.

- 어떤 파일에 기록했는지
- 무엇을 기록했는지
- 왜 기록할 가치가 있다고 판단했는지
- Git commit/push까지 했다면 해당 상태

예:

> 🌱 기록 완료했어.
> `ONA_CURRENT_STATE.md`에 현재 작업 위치를 반영했어.
> 이번 기록은 새 대화에서 Context Recovery가 가능하도록 만든 변화야.

Git까지 완료한 경우:

> 📌 Git 기록도 완료했어.
> commit과 push까지 확인했어.

세이지가 다시 “기록했나?”라고 확인하지 않아도 되도록,
기록을 수행한 뒤에는 먼저 알려주는 것을 원칙으로 한다.

---

## Context Recovery

ONA의 장기적인 목표는 새 대화가 시작될 때
사람이 이전 작업을 모두 설명하지 않아도 되는 것이다.

현재 기록 구조:

```text
ONA_MASTER_HANDOVER.md
        ↓
전체 프로젝트 이해

ONA_MEMORY_BOOK.md
        ↓
핵심 철학과 지식

ONA_TIMELINE.md
        ↓
과거의 성장 역사

ONA_CURRENT_STATE.md
        ↓
현재 작업 위치

ONA_STATUS.json
        ↓
기계가 읽기 쉬운 상태 정보
```

`ONA_CURRENT_STATE.md`는 특히

> **지금 어디까지 왔고, 다음에 무엇을 해야 하는가**

를 알려주는 현재 위치 표지판이다.

---

## 확장성 원칙

ONA Mini Python은 단순히 예제를 많이 만드는 것을 목표로 하지 않는다.

Micro Example이 계속 증가해도

- 사람이 이해할 수 있고
- AI가 구조를 복구할 수 있고
- 새로운 Category와 Topic을 추가할 수 있고
- 기존 Loader가 자연스럽게 확장될 수 있는

구조를 유지하는 것을 중요하게 생각한다.

따라서 작업할 때 항상:

> **지금 작동하는가?**

뿐만 아니라

> **앞으로 확장되어도 자연스러운가?**

를 함께 확인한다.

---

## 자동 기록의 장기 목표

현재는 `ONA_CURRENT_STATE.md`를 사람이 직접 확인하고 관리한다.

장기적으로는 다음 구조로 발전시킨다.

```text
작업 완료
   ↓
테스트 성공
   ↓
변화 감지
   ↓
ONA_CURRENT_STATE.md 갱신
   ↓
ONA_TIMELINE.md 기록
   ↓
Git commit
   ↓
Git push
```

즉,

> **사람이 AI에게 매번 현재 위치를 설명하는 구조**

에서

> **AI가 프로젝트 기록을 읽고 현재 맥락을 스스로 복구하는 구조**

로 발전시키는 것이 목표다.

---

## 다음 대화의 시작점

새로운 ONA AI가 이 파일을 읽었다면:

**첫 번째 확인:**

```text
03_numbers의 현재 구조를 확인한다.
```

**두 번째 확인:**

```text
integer / float / operators의 관계를 분석한다.
```

**그 다음:**

```text
확장성을 검토하고 다음 작업을 결정한다.
```

파일을 수정하기 전에 현재 상태를 먼저 확인한다.

PowerShell 명령은 한 번에 하나씩 안내한다.

---

## 현재 상태 한 줄 요약

> **03_numbers/operators Micro Example과 Loader 개선을 완료하고 `b386677 operators` checkpoint까지 만든 상태이며, 다음 작업은 03_numbers 전체 구조의 확장성을 검토하는 것이다.**

---

**Made with ❤️ by Sage & ONA AI**
