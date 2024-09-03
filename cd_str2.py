

#Getting input via STDIN
userInput = input().strip()

ip_list = list(userInput.split(" "))
res = 1

for i in ip_list:
    res = res * int(i)
    
print(res)


"""You are given two numbers. Your task is to multiply the two numbers and print the answer.

Input Description:
You are given two numbers ‘n’ and ‘m’.

Output Description:
Print the multiplied answer

Sample Input :
99999 99998

Sample Output :
9999700002"""
