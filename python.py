import time

i = 0
while True:
    print("keep coding in python")
    start_time = time.time()
    time.sleep(3)
    end_time = time.time()
    i += 1
    print(f"This loop has been executed {i} times")
    print(f"It took {end_time - start_time} to perform the loop once")