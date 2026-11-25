import os


def build_label():
    object_name = "CAPTCHA"
    era = "c. 2025"
    ritual = "Humans proved they were human"
    task = "by finding traffic lights"
    doubter = "for a machine that doubted them"
    label = f"{object_name}, {era}. {ritual} {task} {doubter}."
    return label


def main():
    label = build_label()
    assert 1 <= len(label) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(label)


if __name__ == "__main__":
    main()
