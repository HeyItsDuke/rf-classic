import os

def get_directory_from_user_or_file(script_name):
    paths_file = f"{script_name}_paths.txt"
    if os.path.exists(paths_file):
        with open(paths_file, "r", encoding="utf-8") as f:
            directory = f.readline().strip()
    else:
        directory = input("Enter the directory to scan for .rfl files: ").strip()
    return directory

def generate_rfl_files(directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(directory):
        if filename.endswith(".rfl"):
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.tbl")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("#Start\n\n")
                f.write(f"//{filename} Table File\n")
                f.write("$Lightmap Clamp Floor: {43, 49, 49}\n")
                f.write("$Lightmap Clamp Ceiling: {229, 229, 229}\n\n")
                f.write("#End\n")
    
    print("Files generated successfully.")

# Main execution
script_name = os.path.splitext(os.path.basename(__file__))[0]
directory = get_directory_from_user_or_file(script_name)
output_directory = os.path.join(directory, "generated")
generate_rfl_files(directory, output_directory)