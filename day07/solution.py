import os


class Directory:
    def __init__(self, name: str, parent: "Directory") -> None:
        self.name = name
        self.parent = parent
        self._sub_directories = {}
        self._files = []

    def add_directory(self, name: str) -> None:
        self._sub_directories[name] = self._sub_directories.get(name, Directory(name, self))

    def get_directory(self, name: str) -> "Directory":
        return self._sub_directories[name]

    def get_all_directories(self) -> list["Directory"]:
        return sorted(self._sub_directories.values(), key=lambda directory: directory.name)

    def add_file(self, name: str, size: int) -> None:
        self._files.append(File(name, size))

    def calculate_total_size(self) -> int:
        size_sub_directories = sum(directory.calculate_total_size() for directory in self._sub_directories.values())
        size_files = sum(file.size for file in self._files)
        return size_sub_directories + size_files


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


def read_input() -> str:
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
        return f.read()


def is_new_command(line: str) -> bool:
    return line.startswith("$")


def set_up_root_directory() -> Directory:
    root_directory = current_directory = Directory("/", None)
    terminal_input_output = read_input().splitlines()
    for current_line in terminal_input_output:
        if is_new_command(current_line):
            current_command = current_line.split()[1]
            if current_command == "cd":
                directory_name = current_line.split()[2]
                if directory_name == root_directory.name:
                    current_directory = root_directory
                elif directory_name == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.get_directory(directory_name)
            elif current_command == "ls":
                pass
        else:
            type_size, name = current_line.split()
            if type_size == "dir":
                current_directory.add_directory(name)
            else:
                current_directory.add_file(name, int(type_size))

    return root_directory


def find_directories_with_size_less_than(directory: Directory, max_size: int) -> list["Directory"]:
    directories = []
    if directory.calculate_total_size() <= max_size:
        directories.append(directory)
    for sub_directory in directory.get_all_directories():
        directories.extend(find_directories_with_size_less_than(sub_directory, max_size))
    return directories


def find_directories_with_size_of_at_least(directory: Directory, min_size: int) -> list["Directory"]:
    directories = []
    if directory.calculate_total_size() >= min_size:
        directories.append(directory)
    for sub_directory in directory.get_all_directories():
        directories.extend(find_directories_with_size_of_at_least(sub_directory, min_size))
    return directories


def solve_puzzle_1() -> int:
    root_directory = set_up_root_directory()
    directories = find_directories_with_size_less_than(root_directory, 100000)
    return sum(directory.calculate_total_size() for directory in directories)


def solve_puzzle_2() -> int:
    root_directory = set_up_root_directory()
    total_file_system_size = 70000000
    required_update_free_space = 30000000
    current_free_space = total_file_system_size - root_directory.calculate_total_size()
    required_space_to_free = required_update_free_space - current_free_space
    directories = find_directories_with_size_of_at_least(root_directory, required_space_to_free)
    return min(directory.calculate_total_size() for directory in directories)


if __name__ == "__main__":
    print(f"Solution puzzle 1: {solve_puzzle_1()}")
    print(f"Solution puzzle 2: {solve_puzzle_2()}")