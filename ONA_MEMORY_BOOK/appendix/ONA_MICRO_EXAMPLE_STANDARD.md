# ONA Micro Example Standard v1.0

## Purpose

이 문서는 ONA Python 지식 라이브러리의 모든 Micro Example이 따를 공통 규칙을 정의한다.

목표는 작은 예제를 사람이 쉽게 배우고, ONA Loader가 안정적으로 읽고, 새로운 사람이나 AI가 같은 구조로 확장할 수 있게 만드는 것이다.

---

## 1. Terms

### Category

큰 학습 단계다.

예:

- `01_basics`
- `02_strings`

### Topic

하나의 개념을 다루는 학습 폴더다.

예:

- `variables`
- `slicing`

### Micro Example

Topic 안에 있는 실행 가능한 Python 파일 하나다.

예:

- `001_variable_create.py`

---

## 2. Required Topic Structure

모든 Topic은 아래 구조를 가진다.

```text
category/
  topic/
    README.md
    metadata.json
    001_example_name.py
    002_example_name.py
```

필수 항목:

- `README.md`: 사람이 읽는 학습 안내
- `metadata.json`: 프로그램과 검색 기능이 읽는 구조화된 정보
- 하나 이상의 `.py` 파일: 실제 Micro Example

---

## 3. File Naming Rules

Python 예제 파일은 다음 규칙을 따른다.

```text
001_snake_case.py
```

- 번호는 `001`부터 시작한다.
- 번호는 권장 학습 순서를 나타낸다.
- 이름은 기능이 드러나는 영어 `snake_case`를 사용한다.
- 기존 예제 번호는 가능하면 유지한다.

---

## 4. Code Rules

각 Micro Example은 다음을 만족해야 한다.

- 하나의 핵심 개념을 설명한다.
- 다른 예제 없이 단독 실행할 수 있다.
- 초보자가 이해할 수 있는 한국어 주석을 포함한다.
- 실행 결과가 예측 가능하다.
- 기본적으로 외부 라이브러리를 사용하지 않는다.
- 사용자 입력이 필요하면 metadata에 `interactive: true`를 기록한다.

---

## 5. README Standard

각 Topic의 README는 다음 정보를 포함한다.

```md
# topic_name

## 학습 목표

## 선수 지식

## 학습 순서

## 예제 목록

## 난이도
```

초기 Topic은 선수 지식이 없을 수 있다.

---

## 6. Metadata Standard

새로 만들거나 갱신하는 Topic의 `metadata.json`은 다음 구조를 따른다.

```json
{
  "schema_version": "1.0",
  "category": "02_strings",
  "topic": "slicing",
  "title": "문자열 슬라이싱",
  "description": "문자열에서 원하는 구간을 잘라 가져오는 예제",
  "level": "beginner",
  "prerequisites": ["creation", "indexing"],
  "examples": [
    {
      "order": 1,
      "id": "slice_start_end",
      "file": "001_slice_start_end.py",
      "title": "시작과 끝 위치 지정",
      "goal": "[시작:끝] 형식을 이해한다.",
      "interactive": false
    }
  ]
}
```

`metadata.json`은 Topic 안의 예제 목록에 대한 기준 정보다.

---

## 7. Index Standard

`micro_examples/index.json`은 Topic을 찾기 위한 목록이다.

새 표준에서는 상세 예제 목록을 중복해 보관하지 않고, 각 Topic의 `metadata.json`을 기준으로 사용한다.

```json
{
  "schema_version": "1.0",
  "topics": [
    {
      "category": "02_strings",
      "topic": "slicing",
      "path": "02_strings/slicing",
      "metadata_file": "02_strings/slicing/metadata.json"
    }
  ]
}
```

---

## 8. Creation and Review Flow

```text
새 Topic 결정
  ↓
폴더 생성
  ↓
README와 metadata 작성
  ↓
Micro Example 작성
  ↓
문법·경로·메타데이터 점검
  ↓
index.json 등록
  ↓
Git Commit
```

---

## 9. Migration Policy

이 표준은 v1.0부터 새로 만들거나 갱신하는 Topic에 적용한다.

기존 Topic은 학습 내용 변경 없이 단계적으로 표준 구조로 옮긴다. 이전 형식의 index와 metadata는 ONA Loader 구현 전에 한 번에 정리한다.

---

## Last Update

2026-08-07

ONA Micro Example Standard v1.0 established.
