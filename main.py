import os

JOKE = (
    "Dimas emptied 214 desks in four minutes flat — the best-run meeting "
    "of the quarter. There was no fire drill; he'd pulled the alarm himself "
    "to end the budget review."
)


def main():
    # One-line limit for this competition is 200 characters; this joke is 164.
    assert 1 <= len(JOKE.strip()) <= 200, len(JOKE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
