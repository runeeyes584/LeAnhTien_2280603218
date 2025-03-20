from Crypto.Hash import SHA3_256

def sha3(input_string):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(input_string)
    return sha3_hash.hexdigest()

def main():
    text = input("Enter the string to hash: ").encode('utf-8')
    sha3_hash = sha3(text)
    
    print("Chuỗi văn bản đã nhập: ", text.decode('utf-8'))
    print("Ma băm SHA-3 của chuỗi văn bản trên là:", sha3_hash)

if __name__ == "__main__":
    main()