def simple_crypt(message: str, key: str) -> str:
    ret = []
    num_key = 0
    for l in key:
        num_key += ord(l)

    for l in message:
        ret.append(chr(ord(l) ^ num_key))
    
    return "".join(ret)

def rotation_crypt(message: str, key: str) -> str:
    ret = []
    carrousel = []
    index = 0
    for l in key:
        carrousel.append(ord(l))
    
    for l in message:
        ret.append(chr(ord(l) ^ carrousel[index]))
        index +=1
        if(index >= len(carrousel)):
            index = 0

    return "".join(ret)


if __name__ == "__main__":
    import sys    
    try:
        message = sys.argv[1]
    except IndexError:
        message = "A string to be 'encrypted'"
    try:
        key = sys.argv[2]
    except IndexError:
        key = "random_key"

    silent = True

    encryption_method = rotation_crypt
    #encryption_method = simple_crypt
    if(silent):
        print(encryption_method(message, key)) 
    else:
        encrypted = encryption_method(message, key)
        print(f"[Original Message]: {message}")
        print(f"[Original Key]: {key}")
        print()
        print(f"[Encrypted]: {encrypted}")
        with_wrong_key = encryption_method(message, "wrong_key")
        assert with_wrong_key != message
        print(f"[Decrypted with wrong key ('wrong_key')]: {with_wrong_key}")
        decrypted = encryption_method(encrypted, key)
        print(f"[Decrypted with corret key ('fabii')]: {decrypted}")
        assert message == decrypted
