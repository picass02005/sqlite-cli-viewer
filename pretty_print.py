import os
from typing import List, Tuple, Any, Optional


def info(msg: str) -> None:
    print(f"\033[0;32mINFO: {msg}\033[0m")


def warning(msg: str) -> None:
    print(f"\033[0;33mWARNING: {msg}\033[0m")


def error(msg: str) -> None:
    print(f"\033[0;31mERROR: {msg}\033[0m")


def pretty_print_table(
        values: List[Tuple[Any]],
        col_name: Optional[List[str]] = None,
        max_length: int = 20,
        multiline: bool = False,
        end_of_line: str = "\r\n",
        show_number_entries: bool = True
) -> None:
    if not values:
        print("No values to display")
        return

    if col_name is not None:
        if len(col_name) != len(values[-1]):
            warning("There isn't the same number of columns in name and values. Removing column name.")
            col_name = None

    max_sizes = []
    values_str: List[List[str]] = [[str(j) for j in i] for i in values]

    n = os.get_terminal_size().columns

    for i in range(len(values_str[0])):
        assert len((_ := sorted(values_str, key=lambda x: len(x[i])))[0]) == len(_[-1]), (
            ValueError("One value doesn't have the same size as the others"))

        max_sizes.append(len(sorted(values_str, key=lambda x: len(x[i]), reverse=True)[0][i]))

    if col_name is not None:
        for i, j in enumerate(col_name):
            if max_sizes[i] < len(j):
                max_sizes[i] = len(j)

    if sum(max_sizes) + 3 * len(max_sizes) + 1 <= n:
        max_length = n

    else:
        under = [i for i in max_sizes if i <= max_length]
        act = sum(under) + 3 * len(max_sizes) + 1
        if act <= n:
            max_length = max(max_length, (n - act) // (len(max_sizes) - len(under)))

    max_sizes = [min(i, max_length) for i in max_sizes]

    print(("\u250C" + "\u252C".join(["\u2500" * (i + 2) for i in max_sizes]) + "\u2510")[:n])

    # ===== Prints headers if exist ===== #
    if col_name is not None:
        head = " \u2502 ".join(
            [ajust_length(j, min(max_sizes[i], max_length), True) for i, j in enumerate(col_name)]
        )

        print(f"\u2502 {head} \u2502"[:n])
        print(("\u251C" + "\u253C".join(['\u2500' * (i + 2) for i in max_sizes]) + "\u2524")[:n])

    # ===== Prints values ===== #

    if multiline:
        for k in range(len(values_str)):
            line_nb = 1

            for i, j in enumerate(values_str[k]):
                val = []
                for l in j.split(end_of_line):
                    p = min(max_sizes[i], max_length)
                    val.extend([(l[m:m + p]) for m in range(0, len(l), p)])

                values_str[k][i] = "\n".join(val)

                if len(val) > line_nb:
                    line_nb = len(val)

            for l in range(line_nb):
                values_line = [i.split("\n")[l] if l < len(i.split("\n")) else "" for i in values_str[k]]
                v = " \u2502 ".join(
                    [j.ljust(min(max_sizes[i], max_length), " ") for i, j in enumerate(values_line)]
                )

                print(f"\u2502 {v} \u2502")

            if k != len(values_str) - 1:
                print("\u251C" + "\u253C".join(['\u2500' * (i + 2) for i in max_sizes]) + "\u2524")

    else:
        eol = end_of_line.replace("\r", "\\r").replace("\n", "\\n")

        for k in values_str:
            v = " \u2502 ".join(
                [ajust_length(
                    j.replace(end_of_line, eol), min(max_sizes[i], max_length), False
                ) for i, j in enumerate(k)]
            )

            print(f"\u2502 {v} \u2502")

    print(("\u2514" + '\u2534'.join(['\u2500' * (i + 2) for i in max_sizes]) + "\u2518"))

    if show_number_entries:
        print(f"Printed {len(values):_} rows ({len(values) * len(values[-1]):_} values).")


def ajust_length(s: str, n: int, center: bool = False) -> str:
    if len(s) > n:
        return f"{s[:n - 3]}..."

    elif center:
        return s.center(n, " ")

    else:
        return s.ljust(n, " ")
