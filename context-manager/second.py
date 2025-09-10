# a context manager class that opens a file for writing, logs when it enters/exits, and ensures the file is closed.

class SafeFileOps:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print("Initiating File Operations")
        self.file = open(self.file_name, "a")
        return self.file

    def __exit__(self, err_type, err_value, err_tb):
        if err_type:
            print(f"An \033[1;31mERROR\033[0m occured!\n{err_type}\n{err_value}")
        else:
            print("Operations completed \033[32msuccessfully\033[0m.")
        self.file.close()
        print("File Closed.")
        return True
        


safe_file_read = SafeFileOps("./sample.txt")

new_data = "Hope you are doing well 🤞"
with safe_file_read as file:
    data = file.read()

#print(data)

