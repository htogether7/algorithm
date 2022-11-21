if __name__ == "__main__":
    file = open("input.txt", "r")
    n = int(file.readline())
    cheeses = []
    for _ in range(n):
        cheeses.append(int(file.readline()))
    dp_table_cheese = [0]
    dp_table_count = [0]
    dp_table_cheese.append(cheeses[0])
    dp_table_count.append(1)
    for i in range(2,n+1):
        if dp_table_count[-1] == 2:
            if dp_table_cheese[-1] >= dp_table_cheese[-2] + cheeses[i-1]:
                dp_table_cheese.append(dp_table_cheese[-1])
                dp_table_count.append(0)
            else:
                dp_table_cheese.append(dp_table_cheese[-2] + cheeses[i-1])
                dp_table_count.append(dp_table_count[-2]+1)
        else:
            dp_table_cheese.append(dp_table_cheese[-1] + cheeses[i-1])
            dp_table_count.append(dp_table_count[-1]+1)
    
    print(dp_table_cheese[-1])