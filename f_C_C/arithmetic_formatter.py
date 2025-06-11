from pyutils.colors import Colors

def arithmetic_arranger(problems: list, show_answers: bool = False) -> str:
    final_arrangement: str = ""
    space: str = " "
    dash: str = "-"
    max_lines = 4 if show_answers else 3
    if len(problems) <= 5:
        all_sets: list = []
        for problem in problems:
            listed_problem: list = problem.split(" ")
            if not listed_problem[0].isnumeric() or not listed_problem[2].isnumeric():
                return "Error: Numbers must only contain digits."
            elif len(listed_problem[0]) > 4 or len(listed_problem[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            
            if listed_problem[1] not in ("+", "-"):
                return "Error: Operator must be '+' or '-'."
            elif show_answers:
                if "+" == listed_problem[1]:
                    listed_problem.append(str(int(listed_problem[0]) + int(listed_problem[-1])))
                else:
                    listed_problem.append(str(int(listed_problem[0]) - int(listed_problem[-1])))
            all_sets.append(listed_problem)
        for line in range(max_lines):
            for index, a_set in enumerate(all_sets):
                longest_numeral = max(len(a_set[0]), len(a_set[2]))
                if line == 0:
                    final_arrangement += f"{2 * space}{(longest_numeral - len(a_set[0])) * space}{a_set[0]}"
                elif line == 1:
                    final_arrangement += f"{a_set[1]} {(longest_numeral - len(a_set[2])) * space}{a_set[2]}"
                elif line == 2:
                    final_arrangement += f"{(longest_numeral + 2) * dash}"
                elif show_answers:
                    final_arrangement += f"{(longest_numeral + 2 - len(a_set[-1])) * space}{a_set[-1]}"

                if index != (len(all_sets) - 1):
                    final_arrangement += f"{4 * space}"
            if line < 3 and show_answers:
                final_arrangement += "\n"
            elif line < 2:
                final_arrangement += "\n"

        return final_arrangement # FINAL BOSS
    else:
        return f"{Colors.RED}Error: Too many problems.{Colors.RESET}"


test_list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "23 + 4343"]

print(f'\n{arithmetic_arranger(test_list, True)}')
