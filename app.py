import os

print("\033[36m=================================\033[0m")
print("\033[36m==== Files creater by Sabbah ====\033[0m")
print("\033[36m=================================\033[0m")

# Get file names input
files = str(input("\033[33mFiles names separated with comma: \033[0m")).strip()

# Split the file names by comma
file__names = files.split(",")

# Check if the user provided any file names
if len(file__names) == 0 or file__names == ['']:
    print("\033[31mPlease write at least a single file!\033[0m\n")
    exit()

# Get the file extension
files_ext = str(input("\033[33mFiles extension (e.g, txt, php, js): \033[0m")).strip()

# Check for a valid file extension
if files_ext == "":
    print("\033[31mPlease provide an extension!\033[0m\n")
    exit()

# Get the target path
path = str(input("\033[33mPaste the target path: \033[0m")).strip()

# Check if the target path is empty
if path == "":
    print("\033[31mPlease provide a valid path!\033[0m\n")
    exit()

# Create files
for file_name in file__names:
    file_name = file_name.strip()  # Trim any extra spaces
    full__path = os.path.join(path, file_name + "." + files_ext)
    
    # Check if the file already exists
    if os.path.exists(full__path):
        choice = input(f"\033[31mThere is a file with the name '{file_name + '.' + files_ext}'. Do you want to replace it? (yes/no): \033[0m").lower()

        if choice != "yes":
            print(f"\033[33mSkipped file: {full__path}\033[0m")
            continue

    # Try to create or overwrite the file
    try:
        with open(full__path, "w") as file:
            file.write("")
        print(f"Created file > \033[32m{full__path}\033[0m")
    except Exception as e:
        print(f"\033[31mFailed to create > {full__path}: {e}\033[0m")

print("\nTask Completed!\n")
