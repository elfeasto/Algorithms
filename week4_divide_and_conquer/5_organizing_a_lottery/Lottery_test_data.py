import random
import time

def gen_data(num_segs, num_pts):

    segs = gen_segs(num_segs)
    pts = [random.randrange(-10**8, 10**8) for _ in range(num_pts)]
    ans_str = str(num_segs) + " "+ str(num_pts)
    segs_str = ""
    for idx in range(0,len(segs),2):
        segs_str += ( " " + str(segs[idx]) + " " + str(segs[idx + 1]) )
    pts_str = ""
    for pt in pts:
        pts_str += " " + str(pt)
    ans_str += segs_str
    ans_str += pts_str
    return ans_str

def gen_segs(num_segs):
    segs = []
    for _ in range(num_segs):
        left_pt = random.randrange(-10**8, 10**8)
        right_pt = random.randrange(left_pt, 10**8)
        segs.extend([left_pt,right_pt])
    return segs

t1 = time.time()
input = gen_data(50000,50000)



data = list(map(int, input.split()))

n = data[0]
m = data[1]
starts = data[2:2 * n + 2:2]
ends = data[3:2 * n + 2:2]
intervals = [[starts[idx], ends[idx]] for idx in range(len(starts))]
points = data[2 * n + 2:]

print("done")
print(time.time() - t1)