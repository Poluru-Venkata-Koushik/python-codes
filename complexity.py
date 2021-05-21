import time as ti
start=ti.time_ns()
def sqr(n):
    return n*n

print(sqr(100))
end=ti.time_ns()
print(start-end)