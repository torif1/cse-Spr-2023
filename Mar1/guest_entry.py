file_name = '/workspaces/cse-Spr-2023/Mar1/text_files/guest_book.txt'  # Path to File
Done = False
with open(file_name, 'a') as file_object:
    while Done == False:
        name = input("What is your name? ")
        file_object.write(f'{name},\n')
        if name == 'exit':
            break
        print(f'Hello {name}!')
