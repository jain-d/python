import functools

def line_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc: str):
            result = functools.reduce(lambda total, line: total + 1 if line.find(sequence) >= 0 else total + 0, doc.splitlines(), 0)
            return result

        return with_length

    return with_char



# FORMAT ==>     line_with_sequence(char)(length)(doc)      <==

test = "aaaa\nbbbb\nccdd\naabb"

print(line_with_sequence("c")(4)(test))
