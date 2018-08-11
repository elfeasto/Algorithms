import  random
def rand_int():
    return random.randrange(-10**8, 10**8)

num_intervals = 5
num_pts = 5
intervals = [ (rand_int(), rand_int()) for _ in range(num_intervals) ]
pts = [rand_int() for _ in range(num_pts)]

print(intervals)
print(pts)