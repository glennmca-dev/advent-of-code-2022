from aoc import day
from typing import Optional

input = day(7).splitlines()

class Directory:
	def __init__(self, parent: Optional["Directory"] = None):
		self.parent: "Directory" = self if parent is None else parent
		self.directories: dict[str, "Directory"] = {}
		self.files: list[tuple[int, str]] = []
		self.size: int = 0

	def create_sizes(self):
		self.size = sum([file[0] for file in self.files]) + sum([directory.create_sizes() for directory in self.directories.values()])
		return self.size

	def get_sizes(self):
		self.create_sizes()
		sizes = [self.size]

		for directory in self.directories.values():
			sizes += directory.get_sizes()
		
		return sizes

filesystem = Directory()
ref = filesystem

i = 0

while i < len(input):
	command = input[i].split()
	
	if command[1] == "cd":
		match command[2]:
			case "/":
				ref = filesystem
			case "..":
				ref = ref.parent
			case _:
				ref = ref.directories[command[2]]
	elif command[1] != "ls":
		if command[0] == "dir":
			ref.directories[command[1]] = Directory(ref)
		else:
			ref.files.append((int(command[0]), command[1]))

	i += 1

sizes = filesystem.get_sizes()

print(f"Part 1: {sum([size for size in sorted(sizes) if size <= 100000])}")
print(f"Part 2: {next(size for size in sorted(sizes) if size >= sizes[0] - 40000000)}")
