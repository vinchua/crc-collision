from PyCRC.CRC32 import CRC32
from datetime import datetime
from secrets import choice
import string

def main():
    hashes = {}

    t1 = datetime.now()

    while True:
        s = ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(6)])
        hash = CRC32().calculate(s)

        if hash in hashes:
            if s == hashes[hash]:
                continue
            else:
                t2 = datetime.now()
                time_elapsed = t2 - t1
                print(s + " and " + hashes[hash] + " have the same CRC " + str(hash) + ".")
                print("Time elapsed:", str(time_elapsed.seconds) + "." + str(time_elapsed.microseconds), "s")
                print("Calculated", len(hashes), "values.")
                break 

        else:
            hashes[hash] = s
#            print("String: " + s + "\tHash: " + str(hash))


    
    
if __name__ == '__main__':
    main()
