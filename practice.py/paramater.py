x = 1
y = x ** 2 + 2 * x + 1
print("yの評価値:",y)

# 変数xの値を2に変更
x = 2
print("yの評価値:", y)

# yの値は再計算されない

# yの値を再計算
y = x ** 2 + 2 * x + 1
print("yの評価値:", y)

# 入れ替え
x,y = 1,2 
print("xの値:", x,"yの値:", y)
x,y = y,x
print("xの値:", x,"yの値:", y)