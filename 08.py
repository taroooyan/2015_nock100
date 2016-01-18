# coidng: UTF-8
def cipher(string, mode):
    if mode == "encode":
        clipt_text = []
        for s in string:
            if s.islower():
                clipt_text += chr(219-ord(s))

            else:
                clipt_text += s
        return clipt_text
    else:
        text = []
        for s in string:
            if s.islower():
                text += chr(219-ord(s))

            else:
                text += s
        return text

if __name__ == "__main__":
    plain_text = "I am taroooyan"
    print plain_text
    encode_text = cipher(plain_text, "encode")
    print encode_text
    print cipher(encode_text, "decode")
