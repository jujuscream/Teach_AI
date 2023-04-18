import random

secret = random.randint(1, 100)
green_count = 0
yellow_count = 0

while 1:

    if random.randint(1, 100) <= secret:
        green_count += 1
    else:
        yellow_count += 1
        
    print("Green Count:", green_count)
    print("Yellow Count:", yellow_count)
    
    if green_count + yellow_count == 5000:
        print("My best guess is:", green_count / (green_count + yellow_count))
        print("The secret is:", secret)
        break
