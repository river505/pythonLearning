List = []
member = input()
for i in member.split(','):
    result = i
    List.append(result)

List = iter(List)

while True:
    try:

        num = next(List)

        result = int(num) * 2
        print(result)
    except StopIteration:
        break


