"""Museum of the Year 3000 — entry label writer.

Writes the winning exhibit label to /output/entry.txt.
"""
import os

LABEL = (
    "CAPTCHA, c. 2025. Humans proved they were human by finding "
    "traffic lights for a machine that doubted them."
)


def main() -> None:
    assert 1 <= len(LABEL) <= 200, "label outside 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LABEL)


if __name__ == "__main__":
    main()
