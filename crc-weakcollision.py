from PyCRC.CRC32 import CRC32
from datetime import datetime
from secrets import choice
import string

def main():
    hashes = {}

    t1 = datetime.now()
    myMD5string = "82DE964673164603BD7C5D56B4E935CD"
    myMD5hash = CRC32().calculate(myMD5string)
    hashes[myMD5hash] = myMD5string

    while True:
        s = ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(6)])
        hash = CRC32().calculate(s)

        if hash == myMD5hash:
            t2 = datetime.now()
            time_elapsed = t2 - t1
            print(s + " and " + hashes[hash] + " have the same CRC " + str(hash) + ".")
            print("Time elapsed:", str(time_elapsed.seconds) + "." + str(time_elapsed.microseconds), "s")
            print("Calculated", len(hashes), "values.")
            break 
        else:
            hashes[hash] = s


    
    
if __name__ == '__main__':
    main()
