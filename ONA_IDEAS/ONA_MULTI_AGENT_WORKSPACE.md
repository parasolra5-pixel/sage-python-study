# 🌱 ONA Multi-Agent Workspace

> 하나의 ONA 맥락을 여러 ONA AI가 공유하면서, 서로 다른 영역과 관점에서 병렬로 작업하는 아이디어를 기록한다.

## 1. 아이디어

새로운 대화창을 여러 개 열어 각각의 ONA AI에게 서로 다른 작업 영역 또는 관점을 맡긴다.

각 ONA AI는 공통의 `ONA_CURRENT_STATE.md`를 시작점으로 삼아 현재 프로젝트 맥락을 복구한 뒤, 담당 영역을 독립적으로 탐색하고 분석한다.

## 2. 기본 구조

```text
                    ONA_CURRENT_STATE.md
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
           ONA AI A     ONA AI B     ONA AI C
            구조 분석     Loader 분석    기록/철학
              │            │            │
              └────────────┼────────────┘
                           ↓
                    Sage + ONA 통합
```

## 3. 예시: 03_numbers 분석

- **ONA AI A — 구조 담당**
  - `03_numbers` 폴더 구조
  - `integer / float / operators` 관계
  - 중복과 확장성 확인

- **ONA AI B — Loader 담당**
  - `loader.py`
  - Topic 검색
  - Category 충돌 처리
  - 향후 확장성 분석

- **ONA AI C — Metadata 담당**
  - `metadata.json`
  - `index.json`
  - schema 일관성
  - 대규모 Micro Example 확장 가능성

- **ONA AI D — ONA 관점**
  - 사람-AI 협업 구조에 미치는 영향
  - Context Recovery 관점
  - 기록할 가치가 있는 발견 판단

## 4. 중요한 운영 원칙

처음에는 여러 ONA AI가 **읽기 → 분석 → 의견 제시**를 담당한다.

같은 파일을 여러 ONA AI가 동시에 수정하지 않는다.

실제 파일 수정과 Git 반영은 하나의 작업 흐름에서 통합하여 진행한다.

즉, 병렬화하는 것은 **관점과 분석**이고, 최종 변경은 **통합된 하나의 작업 흐름**에서 관리한다.

## 5. ONA와의 연결

이 아이디어는 다음 질문을 실제 환경에서 실험하는 방법이다.

> **어떤 구조가 사람과 AI의 지속적인 협업을 실제로 더 지능적으로 만드는가?**

기존의

> 한 사람 + 한 AI + 하나의 맥락

에서 나아가,

> **한 사람 + 여러 AI 관점 + 하나의 공유된 상태**

를 실험한다.

`ONA_CURRENT_STATE.md`는 여러 ONA AI가 공유하는 **공통 출발점(Context Recovery Entry Point)** 역할을 한다.

## 6. 현재 상태

이것은 아직 확정된 시스템 구조가 아니라 **설계 아이디어 및 실험 후보**이다.

먼저 여러 대화창에서 실제로 서로 다른 영역을 분석해 보고, 효과와 한계를 확인한 뒤 ONA의 정식 구조로 발전시킨다.

---

Made with ❤️ by Sage & ONA AI
