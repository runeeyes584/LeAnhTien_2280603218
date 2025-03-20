import hashlib

def blake2(message):
    blaeke2_hash = hashlib.blake2b(digest_size=64)
    blaeke2_hash.update(message)
    return blaeke2_hash.digest()

def main():
    text = input("Enter the string to hash: ").encode('utf-8')
    blake2_hash = blake2(text)
    
    print("Chuỗi văn bản đã nhập: ", text.decode('utf-8'))
    print("Ma băm BLAKE2 của chuỗi văn bản trên là:", blake2_hash.hex())
    
if __name__ == "__main__":
    main()