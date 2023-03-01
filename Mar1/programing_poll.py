file_name = '/workspaces/cse-Spr-2023/Mar1/text_files/poll_responses.txt'  # Path to File
Done = False
with open(file_name, 'a') as file_object:
    while True:
        name = input("What is your name? ")
        if name == 'exit':  # yes, I know this is ugley
            break
        reason_for_programing = input("Why do you like programing?")
        if reason_for_programing == 'exit':
            break
        file_object.write(f'{name}:{reason_for_programing}\n')
        print('Thank you for your respoonce!')
