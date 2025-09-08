some_text = "* hello world\n- how are you\n* I hope well\n\nanyways, bye."

print("\n".join(filter(lambda line: line[0] != "-" if len(line) > 0 else True, some_text.split("\n"))))
