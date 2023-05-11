

def bitwise_operation(a, b, op):
    if op == '&':
        return a & b
    elif op == '|':
        return a | b
    elif op == '^':
        return a ^ b
    elif op == '<<':
        return a << b
    elif op == '>>':
        return a >> b
    else:
        print('Invalid operator')

a = 0b1100
b = 0b1010
c = bitwise_operation(a, b, '&')
d = bitwise_operation(a, b, '|')
e = bitwise_operation(a, b, '^')
f = bitwise_operation(a, 2, '<<')
g = bitwise_operation(a, 2, '>>')

print(bin(c))
print(bin(d))
print(bin(e))
print(bin(f))
print(bin(g))