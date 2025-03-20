import hashlib

def calculate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

input_string = input("Enter the string to hash: ")
sha256_hash = calculate_sha256(input_string)
print("Ma bam SHA-256 cua {} la: {}".format(input_string, sha256_hash))