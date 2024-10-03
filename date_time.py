import time
from datetime import datetime
i = 1

for i in range(1000000):
    start_time = datetime.now()
    time.sleep(2)
    i += 1
    print(f"this loop has been executed  {i} times")
    end_time = datetime.now()

    print(f"Loop executed in: {end_time - start_time}")