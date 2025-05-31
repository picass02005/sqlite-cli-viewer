import argparse

import db_management
import pretty_print
from commands import Commands

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Open a sqlite database and show a prompt\n"
                    "By default, the opened database is copied in memory to avoid changing it",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "database",
        nargs="?",
        help="File path to the database to open\n"
             "To open a memory database, you can specify :memory:"
    )
    parser.add_argument(
        "--unsafe",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Open the database in unsafe mode\n"
             "When this is used, changes are directly made on your database file\n"
             "By default, your database is copied in memory and only get pushed into your database when closing it"
    )

    args = parser.parse_args()

    if args.database is None:
        parser.print_help()
        exit(0)

    if args.unsafe:
        db = db_management.unsafe_open(args.database)

    else:
        db = db_management.safe_open(args.database)

    cmd = Commands(db)

    on = True

    while on:
        input_str = input(">>> ").strip()

        if input_str.lower() == ".quit" or input_str.lower() == ".q":
            on = args.database != ":memory:"
            commit: bool = False
            while on:
                match input("Would you like to save your changes? (y/n)\n>>> ").lower():
                    case "yes" | "y":
                        commit = True
                        on = False

                    case "no" | "n":
                        on = False

            if args.unsafe:
                if commit:
                    db.commit()

                else:
                    db.rollback()

                db_management.unsafe_close(db)

            else:
                if commit:
                    db_management.safe_close(db, args.database)

                else:
                    db.close()

            pretty_print.info("Database closed")

        else:
            cmd.process_command(input_str)
