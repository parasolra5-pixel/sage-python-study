import os
import json


CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


BASE_PATH = os.path.abspath(
    os.path.join(
        CURRENT_DIR,
        "../../micro_examples"
    )
)


INDEX_FILE = os.path.join(
    BASE_PATH,
    "index.json"
)


def create_structure(template_file):

    with open(
        template_file,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)


    category = data["category"]
    topic = data["topic"]
    examples = data["examples"]


    target_path = os.path.join(
        BASE_PATH,
        category,
        topic
    )


    os.makedirs(
        target_path,
        exist_ok=True
    )


    create_python_files(
        target_path,
        examples
    )


    create_readme(
        target_path,
        data
    )


    create_metadata(
        target_path,
        data
    )


    update_index(
        target_path,
        data
    )



def create_python_files(path, examples):

    for index, example in enumerate(
        examples,
        start=1
    ):

        filename = (
            f"{index:03d}_{example}.py"
        )


        filepath = os.path.join(
            path,
            filename
        )


        if not os.path.exists(filepath):

            with open(
                filepath,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    f"# {example}\n\n"
                    "print('ONA Micro Example')\n"
                )

            print(
                f"생성 완료: {filepath}"
            )


        else:

            print(
                f"이미 존재: {filepath}"
            )



def create_readme(path, data):

    filepath = os.path.join(
        path,
        "README.md"
    )


    if not os.path.exists(filepath):

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
f"""# {data['topic']}

설명:
{data['description']}

난이도:
{data['level']}

ONA Micro Example
"""
            )

        print(
            "README 생성 완료"
        )



def create_metadata(path, data):

    filepath = os.path.join(
        path,
        "metadata.json"
    )


    if not os.path.exists(filepath):

        metadata = {

            "category":
                data["category"],

            "topic":
                data["topic"],

            "description":
                data["description"],

            "level":
                data["level"],

            "examples":
                data["examples"]

        }


        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                metadata,
                file,
                ensure_ascii=False,
                indent=4
            )


        print(
            "metadata 생성 완료"
        )





def update_index(path, data):

    if os.path.exists(INDEX_FILE):

        try:

            with open(
                INDEX_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                index = json.load(file)


        except json.JSONDecodeError:

            print(
                "index.json 오류 발견 → 새로 생성합니다"
            )

            index = []


    else:

        index = []


    relative_path = os.path.relpath(
        path,
        BASE_PATH
    )


    files = []

    for filename in os.listdir(path):

        if filename.endswith(".py"):

            files.append(filename)


    item = {

        "category":
            data["category"],

        "topic":
            data["topic"],

        "description":
            data["description"],

        "level":
            data["level"],

        "path":
            relative_path.replace("\\", "/"),

        "files":
            files

    }


    updated = False


    for old in index:

        if old["path"] == item["path"]:

            old.update(item)

            updated = True


    if not updated:

        index.append(item)


    with open(
        INDEX_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            index,
            file,
            ensure_ascii=False,
            indent=4
        )


    print(
        "index.json 업데이트 완료"
    )
if __name__ == "__main__":

    create_structure(
        "micro_template.json"
    )