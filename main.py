import sqlite3
import argparse

from process_command import process_command
from commands import Commands

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Open a sqlite database and show a prompt")
    parser.add_argument(
        "database",
        nargs="?",
        help="File path to the database to open"
    )

    args = parser.parse_args()

    if args.database is None:
        parser.print_help()
        exit(0)

    db = sqlite3.connect(args.database)
    cmd = Commands(db)

    on = True

    while on:
        input_str = input(">>> ").strip()

        if input_str.lower() == ".quit" or input_str.lower() == ".q":
            on = cmd.quit()

        else:
            process_command(input_str, cmd)
