import sqlite3

import pretty_print


def unsafe_open(fp: str) -> sqlite3.Connection:
    pretty_print.warning(f"Opening {fp} in unsafe mode")

    return sqlite3.Connection(fp)


def unsafe_close(db: sqlite3.Connection) -> None:
    db.commit()
    db.close()


def safe_open(fp: str) -> sqlite3.Connection:
    pretty_print.info(f"Copying {fp} content into memory...")

    original = sqlite3.connect(fp)
    db = sqlite3.connect(":memory:")

    # Copy original db into memory db
    db.executescript("".join(line for line in original.iterdump()))

    original.close()

    pretty_print.info("Database opened in safe mode")

    return db


def safe_close(db: sqlite3.Connection, fp: str) -> None:
    pretty_print.info(f"Copying modified database from memory into {fp}")

    with open(fp, "w"):
        pass

    original = sqlite3.connect(fp)
    original.executescript("".join(line for line in db.iterdump()))

    original.close()
    db.close()
