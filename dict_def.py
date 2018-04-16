#使用字典来储存操作
functions = {
    'sum' : lambda x,y: x+y,
    'subtract' : lambda x,y: x-y
}
print(functions['sum'](9,3))
print(functions['subtract'](11,5))
