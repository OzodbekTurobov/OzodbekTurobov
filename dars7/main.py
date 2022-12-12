yosh = input("yoshingizni kiriting: ")
try:
    yosh = int(yosh) # Xato qaytargan qator
    print(f"Siz {2022-yosh} chi yilda tugu`lgansiz ")
except: # Xato yuz bergan bajariluvchi kod
    print("Butun son, kiritmadingiz.")

print("Dastur Tugadi, sox bo`ling!.")