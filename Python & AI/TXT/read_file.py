"""# Read a file line by line
with open(r"C:\Users\dieag\OneDrive\Documentos\DIEGO\Classes\Platzi\Python e Inteligencia Artificial\TXT\caperucita.txt", "r") as file:
    for lineas in file:
        print(lineas.strip()) #strip() elimina los saltos de línea
# Read a file in a list
with open(r"C:\Users\dieag\OneDrive\Documentos\DIEGO\Classes\Platzi\Python e Inteligencia Artificial\TXT\caperucita.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    """
 # Write a file   
"""   with open(r'C:\Users\dieag\OneDrive\Documentos\DIEGO\Classes\Platzi\Python e Inteligencia Artificial\TXT\caperucita.txt', 'a') as file:
        file.write("\n\nBy:ChatGPT2")
"""
with open("caperucita.txt","w") as file:
    file.write("Erase me")
    
with open ("clase30/caperucita.txt", "r") as file:
    lines = file.readlines()
    print(len(lines)) # 63