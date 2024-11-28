from fake_math import divide as fake_division
from true_math import divide as true_division

result1=fake_division(48, 6)
result2=fake_division(78, 0)
result3=true_division(24, 8)
result4=true_division(11, 0)

print(result1)
print(result2)
print(result3)
print(result4)