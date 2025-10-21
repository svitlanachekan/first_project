# print('''
#    _~_        
#   (o o)      
#  /  V  \    
# /(  +'''n'''+  )\  
#   ^^ ^^      
#   ''', end='')

n = int(input())
n = 5
str_n = "123456789"

#    _~_              
#   (o o)      
#  /  V  \    
# /(  +'''n'''+  )\  
#   ^^ ^^      
#   ''', end='')

# print("    _~_    " * n)
# print("   (o o)   " * n)
# print(r"  /  V  \  " * n)
# if n == 1:
#     number = "/(  "+ str(n) +r"  )\ "
# print("/(  "+ str(n) +r"  )\ "  ) 
# print(number * n)
# print("  ^^ ^^  " * n)

p1 = "    _~_    " 
p2 = "   (o o)   " 
p3 = "  /  V  \  " 
p5 = "   ^^ ^^  "

print(p1 * n)
print(p2 * n)
print(p3 * n)

nums = "1 2 3 4 5 6 7 8 9"[:2*n]
p4 = + str(n) +r"  )\ ".join(nums.split())


print("/(  "+ str(n) +r"  )\ "  ) 
print(number * n)
print("  ^^ ^^  " * n)