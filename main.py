Placeholder="[name]"

with open("./Input/Names/invited_names.txt") as invited_name:
    name=invited_name.readlines()
    print(name)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content=letter_file.read()

for names in name:

    stripped_names=names.strip()
    new_placeholder=letter_content.replace(Placeholder,stripped_names)
    print(new_placeholder)
    with open(f"./Output/ReadyToSend/letter_to_{stripped_names}.txt","w") as Readytosendfile:
        Readytosendfile.write(new_placeholder)
