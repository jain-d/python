class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return "You can use this value inside 'as'"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return False  # Propagate exception (True would suppress it)


print("\n\033[32mInitializing...\033[0m\n\n")

my_context_manager = MyContextManager()

with my_context_manager as value:
    print(f"Inside the context manager using \033[32mwith\033[0m '{value}'")
    raise Exception("fake exception to test the behavior")

print("\n\n\033[31mClosing...\033[0m\n\n")
