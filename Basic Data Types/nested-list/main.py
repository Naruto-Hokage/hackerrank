if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        records.sort(key=lambda x: x[1])
    lowest = records[0][1]
    for item in records:
        if item[1] > lowest:
            lowest = item[1]
            break
    lowest_array = [[name, value] for name, value in records if value == lowest]
    lowest_array.sort(key=lambda x: x[0])
    for item in lowest_array:
        print(item[0])
