# val = int(input())
# output = "Weird"
# if val%2 == 1:
#     pass
# elif 2 <= val < 5:
#     output = "Not Weird"
# elif 6 <= val <= 20:
#     pass
# else:
#     output = "Not Weird"

# print(output)

n = int(raw_input())

if n%2 == 1:
   print('Weird')
elif n>=2 and n<=5:
    print('Not Weird')
elif n>=6 and n<=20:
    print('Weird')
elif n>20: 
    print('Not Weird')