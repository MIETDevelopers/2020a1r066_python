database=[('diya', 1, 'diyagupta676@gmail.com', 'female', '2/10/2002', 'jammu', '5th', 'A1', 1234567890), ('raghav', 2, 'raghav0191@gmail.com', 'male', '01/12/2002', 'jammu', '5th', 'A1', 1243576890)]

def querying():
    print("Getting available information of student in database:\n")
    for idx,element in enumerate(database):
        print(f"name:{database[idx][0]}")
        print(f"rollno:{database[idx][1]}")
        print(f"email:{database[idx][2]}")
        print(f"gender:{database[idx][3]}")
        print(f"d.o.b:{database[idx][4]}")
        print(f"address:{database[idx][5]}")
        print(f"semester:{database[idx][6]}")
        print(f"section:{database[idx][7]}")
        print(f"phoneno:{database[idx][8]}\n")

querying()
