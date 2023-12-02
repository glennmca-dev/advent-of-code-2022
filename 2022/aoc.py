def day(day: int) -> str:
	with open(f"./test{day}.txt") as file:
		return file.read()