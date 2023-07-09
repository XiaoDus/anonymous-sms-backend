import random
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
print(''.join(random.choice(chars) for i in range(16)))