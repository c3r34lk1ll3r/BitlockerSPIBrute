import csv
import argparse
def main(args):
    with open(args.s, 'r') as s:
        spi = csv.reader(s, delimiter = ',')
        header = None
        lines = []
        for row in spi:
            if header == None:
                header = row
                continue
            i= 0
            line = {}
            while i < len(row):
                line[header[i]] = row[i]
                i+=1
            lines.append(line)

    miso = open(args.o+'.miso','w')
    mosi = open(args.o+'.mosi', 'w')
    for line in lines:
        miso.write(line['MISO'][2:])
        mosi.write(line['MOSI'][2:])
    miso.close()
    mosi.close()
msg = "Extract from Saleae Logic the single channel from CSV"
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = msg)
    parser.add_argument('-s', help="SPI dump file")
    parser.add_argument('-o', help='Output File')
    args = parser.parse_args()
    main(args)
