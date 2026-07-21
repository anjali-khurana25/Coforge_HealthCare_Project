even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0

print("Even Numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        even_sum += i
        even_count += 1

print("\n")

print("Odd Numbers:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
        odd_sum += i
        odd_count += 1

print("\n")

even_avg = even_sum / even_count
odd_avg = odd_sum / odd_count

print("Count of Even Numbers:", even_count)
print("Count of Odd Numbers:", odd_count)
print("Total Count:", even_count + odd_count)

print("Sum of Even Numbers:", even_sum)
print("Sum of Odd Numbers:", odd_sum)

print("Average of Even Numbers:", even_avg)
print("Average of Odd Numbers:", odd_avg)