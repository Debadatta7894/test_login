# csv file_handeling


import csv

# print(dir(csv))

# rows = [
#     ["name","age","city"],
#     ["litu","24","jajpur"],
#     ["deba","23","bari"],
#     ["jiban","22","ctc"]
# ]

# with open("data.csv",'w',newline="") as file1:
#     writer = csv.writer(file1)
#     writer.writerows(rows)

# with open("data.csv","r",newline="") as file2:
#     reader = csv.reader(file2)
#     for i in reader:
#         print(i,end="  ")



# dict reader and dict writer


# data = [
#     {"name":"Debadatta","age":"24","city":"jajpur"},
#     {"name":"litu","age":"23","city":"bhubanswar"},
#     {"name":"deba","age":"22","city":"ctc"},
# ]

# with open("data1.csv","w",newline="") as file3:
#     fields = ["name","age","city"]
#     writer = csv.DictWriter(file3,fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(data)


with open("data1.csv","r") as file4:
    reader = csv.DictReader(file4)
    for i in reader:
        print(i)