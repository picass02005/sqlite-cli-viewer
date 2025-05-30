import sqlite3


class Commands:
    def __init__(self, db: sqlite3.Connection):
        self.db = db

    def quit(self) -> bool:
        print("CHECK IF COMITED OR NOT")

        return False  # Return on state

    def tables(self, input_str: str) -> None:
        if len(args := input_str.split(" ")) > 1:
            arg = f"{input_str[1]}"

        else:
            arg = "%"

        cursor = self.db.execute(
            "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%' AND NAME LIKE ?;",
            (arg,)
        )

        print(cursor.fetchall())
        print("TODO: pretty print")
