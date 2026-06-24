import os
from datetime import datetime
file_name = "data.txt"


with open(file_name, "a") as file:
    file.write(f"Contribution made on: {datetime.now()}\n")

print("File updated. Starting Git commands...")

os.system("git add .")
os.system('git commit -m "chore: automatic green dot commit"')
os.system("git push")

print("Done! Check your GitHub graph.")