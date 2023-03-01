file_name = '/workspaces/cse-Spr-2023/Mar1/text_files/text.txt'  # Path to File
with open(file_name, 'w') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")

file_name = '/workspaces/cse-Spr-2023/Mar1/guest.txt'

with open(file_name, 'w') as file_object:
    file_object.write(input('What is your name: '))
