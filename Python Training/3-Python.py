python = int(input("Enter marks of python: "))
java = int(input("Enter marks of java "))
sql = int(input("Enter marks of sql "))
toc = int(input("Enter marks of toc "))
cn = int(input("Enter marks of cn "))

length = len([python, java, sql, toc, cn])

result = python + java + sql + toc + cn

average = result/length

print(f"the average of the five subjects will be: {average}")

