from os import listdir, linesep
from os.path import isfile, join

path = '../files_to_check'
file_names = [f for f in listdir(path) if isfile(join(path, f))]


files = {}
for name in file_names:
    file = open(join(path, name), 'r')
    file_dict = {}
    for line in file:
        if not line.startswith('#'):
            item_name, item_value = line.rsplit(' ', 1)
            file_dict[item_name] = item_value
    files[name] = file_dict
    file.close()


def get_base_file_name(message):
    print("List of files:")
    position = 1
    names_with_numbers = {}
    for file_name in files:
        print(f'{position}. {file_name}')
        names_with_numbers[position] = file_name
        position += 1
    print()
    choice = input(message)
    if not choice.isdigit():
        get_base_file_name('Probably typo in your input. Write only number end press enter: ')
    if 1 < int(choice) < 2:
        get_base_file_name('Choose from 1 or 2: ')

    return names_with_numbers[int(choice)]


base_file_name = get_base_file_name("Which file should be base? ")
print("Base file is:", base_file_name)
base_file = set(files.pop(base_file_name))
file_with_changes = set(list(files.values())[0])
print("names in base file:", len(base_file))
print("names in other file:", len(file_with_changes))
print()


def print_result(name_list):
    for name in name_list:
        print(name)



print("Now I check to file for difference...")
deleted_names = base_file.difference(file_with_changes)
added_names = file_with_changes.difference(base_file)
print(f'You have {len(added_names)} new names and {len(deleted_names)} deleted\n')
print(f'+1 {len(added_names)} Added names:')
print_result(added_names)
print('_' * 50, '\n')
print(f'-{len(deleted_names)} Deleted names:')
print_result(deleted_names)
print('_' * 50, '\n')
with open('added.txt', 'w') as f1:
    for name in added_names:
        f1.writelines(name + '\n')
# with open('deleted.txt', 'w') as f1:
#     for name in deleted_names:
#         f1.writelines(name)
