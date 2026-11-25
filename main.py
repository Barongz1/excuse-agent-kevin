"""The Excuse Your Agent Gives You — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The excuse: the bug did not arrive with me — it got promoted under my watch.
TEXT = "The bug was already in the code when I found it. I just gave it a promotion and a corner office."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
