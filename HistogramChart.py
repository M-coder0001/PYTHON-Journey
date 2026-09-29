from matplotlib import pyplot as h

x = ["Web Development","Cyber Security","Dana Analyst","AI/ML"]
y = [50,30,40,80,]

h.hist(x, bins=5)
h.title("IT Fields")

h.xlabel("Fields")
h.ylabel("Vacancy")

h.show()