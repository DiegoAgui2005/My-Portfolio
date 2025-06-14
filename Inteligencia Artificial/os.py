import os
#current working directory
"""cwd = os.getcwd()
print("Current working directory, cwd:", cwd)"""

#List the files in the current directory
"""txt_files = [f for f in os.listdir(".") if f.endswith(".csv")]
print("Files with .txt extension:", txt_files)
"""

os.rename("products.csv", "products_renamed.csv")
print("File renamed successfully")


os.rename("products_renamed.csv", "products.csv")

txt_files = [f for f in os.listdir(".") if f.endswith(".csv")]
print("Files with .txt extension:", txt_files)
