lines = []

while True: 
    line = input()
    if line.lower() == 'done': 
        break
    lines.append(line)
print("Chuyển thành in hoa:")
for line in lines: 
    print(line.upper())