# this program takes in a number, and its factor. It then tell us how many successive division till we get a 0.
import string
special_letter = (string.ascii_lowercase.replace("z", "")).replace("a", "za")
special_letters_tuple = tuple(special_letter)

def successive_division(number, divisor) -> list[str]:
    if not (quotient := number // divisor):
        return list(special_letters_tuple[number % divisor])
    result = successive_division(quotient, divisor) if not (remainder := quotient  
    result.append(special_letters_tuple[number % divisor])
    return result



#print(successive_division(50, 26))

inputs = ((24, 26), (50, 26), (76, 26), (102, 26), (726, 26), (752, 26), (1402, 26))
for i in inputs:
    print(i, "".join(successive_division(*i)))
    print(f"\n\n")
