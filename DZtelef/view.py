def op():
    op = int(input(
        " 1 - добваить пользователя \n 2 - вывести таблицу \n 3 - вывести только имя и фамилию \n 4 - отсортировать по именам \n 5 - отсортировать по id \n 6 - выход\n "))
    return op

def add_worker():
    id = int(input("id :"))
    name=input("name :")
    lastname=input("lastname :")
    number=int(input("number :"))
    comments=input("comments :")
    line=f"{id},{name},{lastname},{number},{comments}\n"
    with open("worker_list2.txt","a") as file:
        file.write(line)
    print("сохранено")

def print_table():
    with open("worker_list2.txt","r") as file:
        for line in file.readlines():
            print(line, end="")
def print_only_name():
    with open("worker_list2.txt","r") as file:
        for line in file.readlines():
            temp = line.split(",")
            print(f"Имя - {temp[1]},Фамилия - {temp[2]}")

