question = {
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            },
            "February": {
                "receipt3.txt": None
            }
        }
    }
}

answer = ["/Documents/Proposal.docx", "/Documents/Receipts/January/receipt1.txt", "/Documents/Receipts/January/receipt2.txt", "/Documents/Receipts/February/receipt3.txt"]


def list_files(parent_directory, current_filepath="") -> list[str]:
    file_paths: list[str] = []
    for key, value in parent_directory.items():
        if value == None:
            file_paths.append(f"{current_filepath}/{key}")
        else:
            file_paths.extend(list_files(value, f"{current_filepath}/{key}"))
    return file_paths


if (returned_value := list_files(question)) == answer:
    print("\033[32mPASS\033[0m")
else:
    print(f"\033[1;31mFAIL\033[0m\nexpect\t{answer}\nreturn\t{returned_value}")
