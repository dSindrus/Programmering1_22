print("------------------------------------------------")

with open("text_files/my_novel.txt", "a") as file:              #Parameter "w" overskriver, og "a" legger til
    while True:
        user_input = input(": ")

        if user_input == "q":
            break
        file.write(user_input + "\n")
