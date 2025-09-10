# Modern representation of creating a contextmanager

from contextlib import contextmanager

@contextmanager
def secure_file_ops(file_name):
    try:
        print("\033[33mInitializing\033[0m")
        file = open(file_name, "a")
        yield file
        print("Operation \033[32msuccessful\033[0m.")
    except Exception as e:
        print("An \033[31mError\033[0m occured")
        print(f"Type: {type(e).__name__}")
        print(e)
    finally:
        print("Closing file.")
        file.close()


new_data = "Ok, Bye"
with secure_file_ops("./sample.txt") as file:
#    data = file.read()
    file.write(new_data)
