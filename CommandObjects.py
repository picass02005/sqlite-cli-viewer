import argparse
import sqlite3
from dataclasses import dataclass
from typing import List, TYPE_CHECKING

@dataclass
class CommandConstant:
    db: sqlite3.Connection
    cli_args: argparse.Namespace


@dataclass
class CommandObject:
    aliases: List[str]
    arguments: List[str]
    help_message: str

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        pass
