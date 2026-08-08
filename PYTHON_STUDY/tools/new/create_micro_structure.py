import argparse
import ast
import json
import re
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
BASE_PATH = CURRENT_DIR.parent.parent / "micro_examples"
INDEX_FILE = BASE_PATH / "index.json"
SCHEMA_FILE = CURRENT_DIR / "schemas" / "micro_schema.json"

CATEGORY_PATTERN = re.compile(r"^\d{2}_[a-z0-9_]+$")
NAME_PATTERN = re.compile(r"^[a-z0-9_]+$")
FILE_PATTERN = re.compile(r"^\d{3}_[a-z0-9_]+\.py$")
LEVELS = {"beginner", "intermediate", "advanced"}


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def require_keys(data, keys, label):
    missing = [key for key in keys if key not in data]
    if missing:
        raise ValueError(f"{label}에 필수 항목이 없습니다: {', '.join(missing)}")


def validate_template(data):
    required = [
        "schema_version",
        "category",
        "topic",
        "title",
        "description",
        "level",
        "prerequisites",
        "learning_objectives",
        "examples",
    ]
    require_keys(data, required, "템플릿")

    if data["schema_version"] != "1.0":
        raise ValueError("현재 생성기는 schema_version 1.0만 지원합니다.")
    if not CATEGORY_PATTERN.fullmatch(data["category"]):
        raise ValueError("category는 03_numbers와 같은 형식이어야 합니다.")
    if not NAME_PATTERN.fullmatch(data["topic"]):
        raise ValueError("topic은 영어 snake_case여야 합니다.")
    if data["level"] not in LEVELS:
        raise ValueError("level은 beginner, intermediate, advanced 중 하나여야 합니다.")
    if not isinstance(data["prerequisites"], list):
        raise ValueError("prerequisites는 목록이어야 합니다.")
    if not isinstance(data["learning_objectives"], list) or not data["learning_objectives"]:
        raise ValueError("learning_objectives는 비어 있지 않은 목록이어야 합니다.")
    if not isinstance(data["examples"], list) or not data["examples"]:
        raise ValueError("examples는 비어 있지 않은 목록이어야 합니다.")

    orders = set()
    ids = set()
    files = set()

    for example in data["examples"]:
        require_keys(
            example,
            ["order", "id", "file", "title", "goal", "interactive"],
            "예제",
        )
        if not isinstance(example["order"], int) or example["order"] < 1:
            raise ValueError("예제 order는 1 이상의 정수여야 합니다.")
        if not NAME_PATTERN.fullmatch(example["id"]):
            raise ValueError("예제 id는 영어 snake_case여야 합니다.")
        if not FILE_PATTERN.fullmatch(example["file"]):
            raise ValueError("예제 file은 001_example.py 형식이어야 합니다.")
        expected_file = f"{example['order']:03d}_{example['id']}.py"
        if example["file"] != expected_file:
            raise ValueError(f"예제 file은 order와 id에 맞아야 합니다: {expected_file}")
        if not isinstance(example["interactive"], bool):
            raise ValueError("예제 interactive는 true 또는 false여야 합니다.")
        if example["order"] in orders or example["id"] in ids or example["file"] in files:
            raise ValueError("예제 order, id, file은 중복될 수 없습니다.")

        orders.add(example["order"])
        ids.add(example["id"])
        files.add(example["file"])


def build_metadata(data):
    metadata = {key: value for key, value in data.items() if key != "examples"}
    metadata["examples"] = []

    for example in sorted(data["examples"], key=lambda item: item["order"]):
        metadata["examples"].append(
            {key: value for key, value in example.items() if key != "starter_code"}
        )

    return metadata


def validate_metadata(metadata):
    schema = load_json(SCHEMA_FILE)
    require_keys(metadata, schema["required"], "metadata")

    unexpected_keys = set(metadata) - set(schema["properties"])
    if unexpected_keys:
        raise ValueError(
            "metadata에 표준에 없는 항목이 있습니다: "
            + ", ".join(sorted(unexpected_keys))
        )

    if metadata["schema_version"] != schema["properties"]["schema_version"]["const"]:
        raise ValueError("metadata schema_version이 schema와 다릅니다.")
    if not CATEGORY_PATTERN.fullmatch(metadata["category"]):
        raise ValueError("metadata category 형식이 올바르지 않습니다.")
    if not NAME_PATTERN.fullmatch(metadata["topic"]):
        raise ValueError("metadata topic 형식이 올바르지 않습니다.")
    if metadata["level"] not in schema["properties"]["level"]["enum"]:
        raise ValueError("metadata level이 올바르지 않습니다.")

    example_schema = schema["properties"]["examples"]["items"]
    for example in metadata["examples"]:
        require_keys(example, example_schema["required"], "metadata 예제")
        unexpected_example_keys = set(example) - set(example_schema["properties"])
        if unexpected_example_keys:
            raise ValueError(
                "metadata 예제에 표준에 없는 항목이 있습니다: "
                + ", ".join(sorted(unexpected_example_keys))
            )
        if not FILE_PATTERN.fullmatch(example["file"]):
            raise ValueError("metadata 예제 file 형식이 올바르지 않습니다.")
def validate_python_files(target_path, examples):
    for example in sorted(examples, key=lambda item: item["order"]):
        file_path = target_path / example["file"]

        if not file_path.exists():
            raise FileNotFoundError(
                f"예제 파일이 존재하지 않습니다: {file_path}"
            )

        source = file_path.read_text(encoding="utf-8")

        try:
            ast.parse(source, filename=str(file_path))
        except SyntaxError as error:
            raise ValueError(
                f"Python 문법 오류: {file_path}\n"
                f"{error}"
            ) from error

        print(f"문법 검사 통과: {file_path}")

def create_python_files(target_path, examples):
    for example in sorted(examples, key=lambda item: item["order"]):
        file_path = target_path / example["file"]

        if file_path.exists():
            print(f"이미 존재: {file_path}")
            continue

        starter_code = example.get("starter_code")
        if not starter_code:
            starter_code = f"# {example['title']}\n# 목표: {example['goal']}\n\nprint('ONA Micro Example')\n"

        file_path.write_text(starter_code, encoding="utf-8")
        print(f"생성 완료: {file_path}")


def create_readme(target_path, data):
    file_path = target_path / "README.md"

    prerequisites = data["prerequisites"] or ["없음"]
    examples = sorted(data["examples"], key=lambda item: item["order"])

    lines = [
        f"# {data['topic']}",
        "",
        "## 학습 목표",
        *[f"- {item}" for item in data["learning_objectives"]],
        "",
        "## 선수 지식",
        *[f"- {item}" for item in prerequisites],
        "",
        "## 학습 순서",
        *[f"{item['order']}. {item['title']}" for item in examples],
        "",
        "## 예제 목록",
        *[f"- `{item['file']}`: {item['goal']}" for item in examples],
        "",
        "## 난이도",
        data["level"],
        "",
        "ONA Micro Example",
        "",
    ]

    file_path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print(f"README 생성/갱신 완료: {file_path}")

def create_metadata(target_path, metadata):
    file_path = target_path / "metadata.json"

    if file_path.exists():
        print(f"이미 존재: {file_path}")
        return

    file_path.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"metadata 생성 완료: {file_path}")


def update_index(target_path, metadata):
    if INDEX_FILE.exists():
        try:
            index = load_json(INDEX_FILE)
        except json.JSONDecodeError:
            print("index.json 오류 발견 → 새 배열로 생성합니다.")
            index = []
    else:
        index = []

    if not isinstance(index, list):
        raise ValueError("현재 index.json은 배열 구조여야 합니다.")

    relative_path = target_path.relative_to(BASE_PATH).as_posix()
    item = {
        "category": metadata["category"],
        "topic": metadata["topic"],
        "description": metadata["description"],
        "level": metadata["level"],
        "path": relative_path,
        "files": [example["file"] for example in metadata["examples"]],
    }

    for position, old_item in enumerate(index):
        if old_item.get("path") == relative_path:
            index[position] = item
            break
    else:
        index.append(item)

    INDEX_FILE.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("index.json 업데이트 완료")


def create_structure(template_path):
    data = load_json(template_path)
    validate_template(data)

    metadata = build_metadata(data)
    validate_metadata(metadata)

    target_path = BASE_PATH / data["category"] / data["topic"]
    target_path.mkdir(parents=True, exist_ok=True)

    create_python_files(target_path, data["examples"])
    validate_python_files(target_path, data["examples"])
    create_readme(target_path, data)
    create_metadata(target_path, metadata)
    update_index(target_path, metadata)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Create an ONA Micro Example Topic.")
    parser.add_argument(
        "--template",
        type=Path,
        default=CURRENT_DIR / "micro_template.json",
        help="Path to a Micro Example template JSON file.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_arguments()
    create_structure(arguments.template.resolve())
