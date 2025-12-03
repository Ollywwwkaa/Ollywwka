def range(start, end, step=1):
    current = float(start)
    end = float(end)
    if step > 0:
        while current < end:
            yield round(current, 10) 
            current += step
    elif step < 0:
        while current > end:
            yield round(current, 10)
            current += step
    else:
        raise ValueError("step cannot be zero")
for i in range(1, 3, 0.5):
    print(i)