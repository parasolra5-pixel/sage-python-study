import json
import sys
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
BASE_PATH = CURRENT_DIR.parent / "micro_examples"
INDEX_FILE = BASE_PATH / "index.json"


def load_json(path):
    with path.open("r", encoding="utf-8-sig") as file:
        return json.load(file)


def find_topic(topic_name):
    index = load_json(INDEX_FILE)

    # category/topic 형식으로 정확하게 검색
    if "/" in topic_name:
        category, topic = topic_name.split("/", 1)

        for item in index:
            if item["category"] == category and item["topic"] == topic:
                topic_path = BASE_PATH / item["path"]
                metadata_file = topic_path / "metadata.json"
                return load_json(metadata_file)

        return None

    # topic 이름만 입력한 경우
    matches = [
        item for item in index
        if item["topic"] == topic_name
    ]

    if len(matches) == 1:
        topic_path = BASE_PATH / matches[0]["path"]
        metadata_file = topic_path / "metadata.json"
        return load_json(metadata_file)

    if len(matches) > 1:
        print(f"Topic '{topic_name}'이 여러 Category에 존재합니다.")
        print("다음 형식으로 Category를 함께 지정해주세요:")

        for item in matches:
            print(f"- {item['category']}/{item['topic']}")

        return None

    return None


if __name__ == "__main__":
    topic_name = sys.argv[1] if len(sys.argv) > 1 else "integer"
    topic = find_topic(topic_name)

    if topic is None:
        print("Topic을 찾을 수 없습니다.")
    else:
        print(f"Topic: {topic['topic']}")
        print(f"제목: {topic['title']}")
        print(f"설명: {topic['description']}")
        print(f"난이도: {topic['level']}")

        print("\n예제:")

        for example in topic["examples"]:
            print(f"- {example['file']}: {example['title']}")