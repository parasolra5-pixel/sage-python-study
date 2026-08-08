ONA Micro Example System

## 1. Micro Example System의 기본 구조

Micro Example System은 작은 Python 예제를 독립적인 지식 단위로 관리하고,
필요한 예제를 탐색하고 불러올 수 있도록 구조화한다.

---

## 2. metadata.json — Source of Truth

각 Topic의 `metadata.json`은 해당 Micro Example Topic의
구조화된 기준 정보(Source of Truth)로 정의한다.

`metadata.json`은 다음 정보를 관리한다.

- Topic 기본 정보
- 학습 수준
- 선수 지식
- 학습 목표
- Micro Example 목록
- 각 Example의 파일 위치와 학습 목적

실제 Python 코드는 `.py` 파일에 존재하며,
metadata는 해당 코드가 무엇이며 어디에 있는지를 설명한다.

---

## 3. README.md — 파생 문서

`README.md`는 `metadata.json`을 기반으로 생성되는
사람이 읽기 위한 설명 문서로 정의한다.

따라서 `metadata.json`이 변경되면 README도 다시 생성할 수 있어야 한다.

```text
metadata.json
      ↓
   README.md

README는 원본 데이터가 아니라 파생 문서이다.

4. index.json — 탐색용 색인

index.json은 Micro Example 전체를 빠르게 탐색하기 위한
탐색용 색인(index) 으로 정의한다.

상세한 Topic 지식과 예제 메타데이터의 기준 정보는
각 Topic의 metadata.json이 담당한다.

index.json은 다음과 같이 탐색에 필요한 최소 정보를 가진다.

category
topic
description
level
path
files

따라서 index.json은 상세 지식의 원본이 아니라
Micro Example Knowledge System의 탐색 지도로 취급한다.

5. Index 무결성 검증

향후 Loader 구현 단계에서 index.json의 항목과
실제 디렉터리 및 파일 구조가 일치하는지
무결성 검증(integrity validation) 기능을 추가한다.

검증 대상은 다음과 같다.

index.json
    ↓
category / topic 확인
    ↓
실제 Topic 디렉터리 존재 확인
    ↓
metadata.json 존재 확인
    ↓
index에 기록된 Python 파일 존재 확인

이를 통해 index가 실제 Micro Example 구조와
불일치하는 상황을 탐지할 수 있도록 한다.

6. 전체 데이터 흐름
metadata.json
      │
      │ Source of Truth
      ↓
index.json ─────→ 탐색용 색인
      │
      ↓
    Loader
      │
      ↓
실제 Micro Examples

README는 별도의 사람용 파생 문서로 관리한다.

metadata.json
      │
      └────────→ README.md
                   사람에게 설명
7. 설계 결정

Micro Example System은 다음 원칙을 따른다.

metadata.json은 Topic의 구조화된 기준 정보(Source of Truth)이다.
README.md는 metadata에서 생성되는 사람용 파생 문서이다.
index.json은 전체 Micro Example을 빠르게 탐색하기 위한 색인이다.
index.json은 상세 지식의 원본이 아니다.
향후 Loader 단계에서 index와 실제 파일 구조의 무결성을 검증한다.
Loader는 index를 이용해 Topic을 찾고 metadata를 읽은 후 실제 Micro Example에 접근한다.
```
