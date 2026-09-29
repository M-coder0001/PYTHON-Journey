from matplotlib import pyplot as b

x = ["Web Development","Cyber Security","Dana Analyst","AI/ML"]
y = [50,30,40,80]

b.bar(x,y)
b.title("IT Fields")

b.xlabel("Fields")
b.ylabel("Vacancy")

b.show()