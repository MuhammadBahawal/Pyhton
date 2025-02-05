# A lambda function is a small anonymous function (a function without a name). 
# It’s used for short, simple operations where defining a full function isn’t necessary.
# 💡 Syntax:
#       lambda arguments: expression
#    One-liner function
#    Can take multiple arguments
#    Automatically returns the result

sum = lambda a,b:a+b
print(sum(4,5))

sub = lambda a,b:a-b

print(sub(1,2))
