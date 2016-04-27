# coding: utf-8
from ctypes import *

msvcrt = cdll.msvcrt

# python3 에서는 안된다.
# message_string = "hello world!\n"
# msvcrt.printf("Testing: %s", message_string)

# 아래의 3가지 방법중 하나를 사용하면 된다.
# message_string = "hello world!\n"
# msvcrt.printf("Testing: %s".encode('ascii'), message_string.encode('ascii'))

# message_string = b"hello world!\n"
# msvcrt.printf(b"Testing: %s", message_string)

message_string = "hello world!\n"
msvcrt.wprintf("Testing: %s", message_string)