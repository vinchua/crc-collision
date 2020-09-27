# crc-collision

## crc-strongcollision.py
Demonstrate CRC does not have strong collision resistance.
There are inputs x and y where x!=y, s.t. CRC(x) == CRC(y)


## crc-weakcollision.py
Demonstrate CRC does not have weak collision resistance.
Using a preset input string x, find another input y, y!=x s.t. CRC(x)==CRC(y)
