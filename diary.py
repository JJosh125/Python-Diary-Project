###Personal Diary Code File 

##cd in working directory 

##Libraries to load/import 

import json
from datetime import datetime
from pathlib import Path

##Setting up the file path 

DIARY_FILE = Path("diary.json")

##Loading previous entries, if they exist 

def load_entries():
    if not DIARY_FILE.exists():
        return []
    try:
        return json.loads(DIARY_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Could not read diary. Starting fresh.")
        return []
    
##Setting up "save" function for diary 

def save_entries(entries):
    DIARY_FILE.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8"
    )

##Setting up functions for the diary "menu"

#Adding entries function 
def add_entry(entries):
    print("Write your entry. Enter a blank line to save it.")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    if not lines:
        print("Nothing saved.\n")
        return
    entries.append({
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "text": "\n".join(lines)
    })
    save_entries(entries)
    print("Entry saved.\n")
    
#Viewing entries function 
def view_entries(entries):
    if not entries:
        print("No entries yet.\n")
        return
    for i, entry in enumerate(reversed(entries), start=1):
        print(f"\n{i}. {entry['created_at']}\n{entry['text']}\n{'-' * 40}")

#Main menu function 
def main():
    entries = load_entries()
    print("Personal Diary (local file only)")
    while True:
        choice = input("1. Add  2. View  3. Quit: ").strip()
        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice in {"3", "q", "quit", "exit"}:
            print("Bye. Keep diary.json private.")
            break
        else:
            print("Choose 1, 2, or 3.\n")


##Where the program starts          
if __name__ == "__main__":
    main()
