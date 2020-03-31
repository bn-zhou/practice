import numpy as np



data = np.genfromtxt("sj.txt")
data = data.astype(int)


rating_sum = np.zeros(200)
people_number = np.zeros(200)

for i in data:
    print (i)
    book_id = i[0]-1
    rating_sum[book_id] += i[1]#这边是要从0行开始算 所以上面要减1
    people_number[book_id] += 1



print (rating_sum/people_number)

