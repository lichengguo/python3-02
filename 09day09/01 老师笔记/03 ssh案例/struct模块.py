import struct



# print(struct.pack("i",10000)) # b"\x10'\x00\x00"
# print(len(struct.pack("i",10000))) # b"\x10'\x00\x00"
# print(struct.pack("i",3456)) # b'\x80\r\x00\x00'
# print(len(struct.pack("i",3456))) # b'\x80\r\x00\x00'
# print(struct.pack("i",1)) # b'\x80\r\x00\x00'


temp=struct.pack("i",10000)

print(struct.unpack("i",temp)[0])
