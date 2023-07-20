# s = input("Enter the string: ")

# s.replace(" ", "")
# rev = ""

# for i in range(len(s)):
#     if s[i] == " ":
#         continue
#     else:
#         rev += s[i]
#     print(rev)


n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
result = 0
while n2 != 0:
    result += n1
    n2 -= 1

result = result if (n1 >= 0 and n2 >= 0) or (n1 <= 0 and n2 <= 0) else -result


print(result)