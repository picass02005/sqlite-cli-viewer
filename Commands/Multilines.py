import global_var
from CommandObjects import CommandObject, CommandConstant


class Multiline(CommandObject):
    aliases = ["multiline"]
    arguments = []
    help_message = "Toggle multiline output"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        if global_var.multiline:
            global_var.multiline = False
            print("Desactivated multiline output")

        else:
            global_var.multiline = True
            print("Activated multiline output")
