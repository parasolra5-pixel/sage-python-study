## 현재 완료 상태

✅ ONA_MEMORY_BOOK 구축 중

✅ PYTHON_STUDY/micro_examples 구조 생성

현재 구조:

micro_examples/
├── 01_basics/
├── 02_strings/
└── index.json

현재:

- Topic 9개
- Micro Example 29개
- README.md 존재
- metadata.json 존재
- Python 예제 존재
- index.json 연결 완료

---

## 최근 결정

ONA Micro Example Standard v1.0 설계 완료.

목표:

코드 파일만 저장하는 구조 →
코드 + 설명 + 메타데이터 + 연결 관계를 가진 지식 시스템

---

## 현재 진행 중인 작업

metadata.json Schema v1.0 발전

변경 예정 파일:

PYTHON_STUDY/tools/new/schemas/micro_schema.json

변경:

- 실제 JSON Schema v1.0 적용

---

PYTHON_STUDY/tools/new/micro_template.json

변경:

- 예제 문자열 목록 방식 제거
- 예제 객체 방식 적용

포함:

- order
- id
- file
- title
- goal
- interactive
- starter_code

---

PYTHON_STUDY/tools/new/create_micro_structure.py

변경:

- 새 template 기반 생성
- README 자동 생성
- metadata.json v1.0 생성
- starter_code는 py 파일에만 사용
- 기존 파일 덮어쓰기 금지
- index.json 자동 갱신

---

## 중요한 조건

현재:
01_basics, 02_strings는 수정하지 않음.

새로운 테스트:
03_numbers/integer

를 생성 테스트용으로 사용.

---

## 다음 작업

현재 Codex는 구현 전 설계 확인 단계.

다음:

1. micro_schema.json v1.0 작성
2. micro_template.json 개선
3. create_micro_structure.py 수정
4. 03_numbers/integer 생성 테스트

순서로 진행 예정.

---

이어갈 문장:

"ONA 프로젝트 이어서 하자.
Micro Example Generator v1.0 구현 단계부터 시작하자."
