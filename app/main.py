from os import listdir
from os.path import isfile, join


PATH = '../files_to_check'


def get_data(path):
    file_names = [f for f in listdir(path) if isfile(join(path, f))]
    if len(file_names) < 2:
        return False
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

    return files


def get_base_file_name(message, files):
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
        get_base_file_name('Probably typo in your input. Write only number end press enter: ', files)
    if 1 < int(choice) < 2:
        get_base_file_name('Choose from 1 or 2: ', files)

    return names_with_numbers[int(choice)]


def print_result(name_list, list_type):
    print(f'{len(name_list)} {list_type} names:')
    result_file_name = list_type + '.txt'
    with open(result_file_name, 'w') as f1:
        f1.writelines(f'{len(name_list)} {list_type} names:\n')
        for name in name_list:
            name = name.replace('\n', '')
            print(name)
            f1.writelines(name + '\n')
    print('_' * 50, '\n')


def main():
    files = get_data(PATH)
    if not files:
        print("There are should be 2 files in directory <files_to_check>")
        print("Copy your files to folder and try again")
        return
    base_file_name = get_base_file_name("Which file should be base? ", files)

    print("Base file is:", base_file_name)
    base_file = set(files.pop(base_file_name))
    file_with_changes = set(list(files.values())[0])
    print("names in base file:", len(base_file))
    print("names in other file:", len(file_with_changes))

    print()
    print("Now I check to file for difference...")
    deleted_names = base_file.difference(file_with_changes)
    added_names = file_with_changes.difference(base_file)
    print(f'You have {len(added_names)} new names and {len(deleted_names)} deleted\n')

    print_result(added_names, 'added')
    print_result(deleted_names, 'deleted')


main()
