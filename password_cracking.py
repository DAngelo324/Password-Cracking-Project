
import hashlib

passwords = ['McDonalds95' , 'evolvesecurity5316' , 'Searay22' , 'lollapalooza' , 'NeuquaValley']

with open('sample_hashes.txt', 'w') as file:
    for pwd in passwords:
        md5_hash = hashlib.md5(pwd.encode()).hexdigest()
        sha1_hash = hashlib.sha1(pwd.encode()).hexdigest()
        sha256_hash = hashlib.sha256(pwd.encode()).hexdigest()

        file.write(f"MD5: {md5_hash} - {pwd}\n")
        file.write(f"SHA-1: {sha1_hash} - {pwd}\n")
        file.write(f"SHA-256: {sha256_hash} - {pwd}\n")


print("Hashes saved to sample_hashes.txt")

with open ('sample_hashes.txt' , 'r') as file:
    lines = file.readlines()
    #iterate through each line in the file
for line in lines   :
        #print each line
    print(line.strip())


