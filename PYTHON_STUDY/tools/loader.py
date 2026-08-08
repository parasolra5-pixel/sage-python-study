import json
import sys
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
BASE_PATH = CURRENT_DIR.parent / "micro_examples"

INDEX_FILE = BASE_PATH / "index.json"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def find_topic(topic_name):
    index = load_json(INDEX_FILE)

    for item in index:
        if item["topic"] == topic_name:
            topic_path = BASE_PATH / item["path"]
            metadata_file = topic_path / "metadata.json"

            metadata = load_json(metadata_file)

            return metadata

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