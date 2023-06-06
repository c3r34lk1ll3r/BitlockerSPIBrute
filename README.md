# Bitlocker SPI Bruteforce

## Requirements 
- tqdm
- dislocker

## How to use
``python main.py -c <Track of MISO ASCII> -m <Mount Point> -o <Partition offset in disk image> -d <disk image``

The file MISO should contain in ASCII the MISO track in one line. 

If the capture was done using ``Saleae Logic analyzer`` you may use ``pyton converter.py`` to convert csv.

