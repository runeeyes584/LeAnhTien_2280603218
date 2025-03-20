def left_rotate(value, shift):
    return ((value << shift) & 0xffffffff) | (value >> (32 - shift))

def md5(message):
    
    a = 0x67452301
    b = 0xefcdab89
    c = 0x98badcfe
    d = 0x10325476
    
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, byteorder='little')
    
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(message[j:j+4],'little') for j in range(0, 64, 4)]
        
        a0, b0, c0, d0 = a, b, c, d
        
        for i in range(64):
            if i < 16:
                f = (b & c) | ((~b) & d)
                g = i
            elif i < 32:
                f = (d & b) | ((~d) & c)
                g = (5*i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3*i + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7*i) % 16
                
            temp = d
            d = c
            c = b
            b = b + left_rotate((a + f + 0x5a827999 + words[g]) & 0xffffffff, 3)
            a = temp
            
        a = (a + a0) & 0xffffffff
        b = (b + b0) & 0xffffffff
        c = (c + c0) & 0xffffffff
        d = (d + d0) & 0xffffffff
        
    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)
    
input_string = input("Enter the string to hash: ")
md5_hash = md5(input_string.encode('utf-8'))
print("Ma bam MD5 cua {} la: {}".format(input_string, md5_hash))