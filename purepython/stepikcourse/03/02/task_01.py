import sys
sys.stdin = open("input_01.txt", "r")

#Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
#За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
#Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba",
# после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

#Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a.
# Если операций потребуется более 1000, выведите Impossible.

#Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a,
# или Impossible, если операций потребуется более 1000.

class OperationCounter:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.iter_ = 0


    def string_replace(self, s):
        cnt = s.count(self.a)
        if not cnt:
            return 0
        else:
            if self.iter_ >= 1000:
                return 1000
            self.iter_ += 1
            return self.string_replace(str(s).replace(self.a, self.b))

s = str(input())
oc = OperationCounter(str(input()), str(input()))
oc.string_replace(s)
print(oc.iter_)
