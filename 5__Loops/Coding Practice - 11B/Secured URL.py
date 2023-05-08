url = input()

secure = False

if url[:5] == 'https':
    secure = True

print(secure)