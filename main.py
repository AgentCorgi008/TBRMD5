import hashlib

for f in range(2):
    print("Enter a password ->", end=" ")
    pass_code = input()
    for s in range(10):
        pass_code = hashlib.md5(pass_code.encode('utf-8')).hexdigest()
    print("Code md5 -> " + pass_code)
