# masking phone number 

ph_number = input("enter phone number - ")
masked = ph_number[-4:].rjust(10, "x")
print(masked)
