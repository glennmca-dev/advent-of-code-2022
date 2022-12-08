def day(day: int) -> str:
	with open(f"./day0{day}.txt") as file:
		return file.read()