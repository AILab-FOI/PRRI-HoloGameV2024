#!/usr/bin/env python3
import os

# Define the path to the modules subdirectory
modules_dir = 'modules'
main_file_path = os.path.join(modules_dir, 'main.py')

# Read the content of the main.py file
with open(main_file_path, 'r') as main_file:
    main_content = main_file.read()

# Split the content of the main.py file at the <TILES> comment
main_content_parts = main_content.split('# <TILES>')

# Prepare the content to be written to the new file
new_file_content = main_content_parts[0]  # Content before <TILES>

# Iterate over the files in the modules directory to append their content
for filename in os.listdir(modules_dir):
    file_path = os.path.join(modules_dir, filename)
    # Skip the main.py file
    if filename == 'main.py' or not filename.endswith('.py'):
        continue
    with open(file_path, 'r') as file:
        new_file_content += '\n' + file.read()  # Append the content of the file

# Append the content from <TILES> to the end of the main.py file
new_file_content += '# <TILES>' + '<TILES>'.join(main_content_parts[1:])

# Write the new content to the hologamep.py file in the current directory
with open('hologamev.py', 'w') as new_file:
    new_file.write(new_file_content)

print("Bundling completed.")

