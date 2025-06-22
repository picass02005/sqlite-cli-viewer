from typing import List

import pretty_print
from CommandObjects import CommandObject, CommandConstant


class Help(CommandObject):
    aliases = ["help", "?"]
    arguments = []
    help_message = "Show help message"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        from CommandsManager import CommandsManager  # Local import to avoid circular import

        commands: List[CommandObject] = CommandsManager.COMMAND_CLASSES
        prefix: str = CommandsManager.COMMAND_PREFIX
        commands.sort(key=lambda x: x.aliases[0])

        Help.pretty_print_commands(commands, prefix)

    @staticmethod
    def pretty_print_commands(commands: List[CommandObject], prefix: str):
        header = ["Command + arguments", "Aliases", "Description"]
        values = []
        for i in commands:
            values.append((
                f"{prefix}{i.aliases[0]} {' '.join(i.arguments)}" if i.arguments else f"{prefix}{i.aliases[0]}",
                f"{' '.join([prefix + j for j in i.aliases[1:]])}" if len(i.aliases) > 1 else "",
                f"{i.help_message}"
            ))

        pretty_print.pretty_print_table(values, header, multiline=True, end_of_line="\n", show_number_entries=False)
