from fractions import Fraction as Fr
franction_1 = str(input())
franction_2 = str(input())
print(f"{franction_1} + {franction_2} = {Fr(franction_1) + Fr(franction_2)}")
print(f"{franction_1} - {franction_2} = {Fr(franction_1) - Fr(franction_2)}")
print(f"{franction_1} * {franction_2} = {Fr(franction_1) * Fr(franction_2)}")
print(f"{franction_1} / {franction_2} = {Fr(franction_1) / Fr(franction_2)}")

