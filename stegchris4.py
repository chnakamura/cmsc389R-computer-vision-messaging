from PIL import Image
import time, argparse, hashlib

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="message to encode")
parser.add_argument("-f", help="image path")
parser.add_argument("-c", help="color field to store image in")
parser.add_argument("-p", help="passphrase")
args = parser.parse_args()

if args.f is None:
    exit("Need to specify image path!")
if args.p is None:
    exit("Need to specify passphrase")
if args.c is None:
    args.c = 0

h = hashlib.sha256()
h.update(args.p)
hashed_passphrase = h.hexdigest()

im = Image.open(args.f, 'r')
width,height = im.size

print hashed_passphrase

def encode_message(msg = "Hello World!"):

    i = 0
    for x in range(0,width,16):
        for y in range(0,height,16):

            if i < len(msg):

                sigma = 0

                s_index = int(hashed_passphrase[i:i+2],base=16)
                s_index_x = x + int(s_index / 16)
                s_index_y = y + int(s_index % 16)

                for a in range(x, x+16):
                    for b in range(y, y+16):
                            if s_index_x != a or s_index_y != b:
                                pixel_values = im.getpixel((x,y))
                                sigma += pixel_values[args.c]

                mean = int(sigma/16**2)

                c = ord(msg[i])
                alpha = mean + int(c/16)
                beta = mean + (c%16)
    
                r,g,b,a = im.getpixel((s_index_x, s_index_y))
                im.putpixel((s_index_x, s_index_y),(alpha,g,b,a))

                r,g,b,a = im.getpixel((s_index_x, s_index_y + 1))
                im.putpixel((s_index_x, s_index_y + 1),(beta,g,b,a))

                print mean
                print(s_index_x, s_index_y)
                print im.getpixel((s_index_x, s_index_y)),im.getpixel((s_index_x, s_index_y + 1))

                time.sleep(.1)
            
            else:

                return

            i += 1

def decode_message():

    msg = ""

    i = 0

    for x in range(0,width,16):
            for y in range(0,height,16):

                sigma = 0

                s_index = int(hashed_passphrase[i:i+2],base=16)
                s_index_x = x + int(s_index / 16)
                s_index_y = y + int(s_index % 16)

                for a in range(x, x+16):
                    for b in range(y, y+16):
                            if s_index_x != a or s_index_y != b:
                                pixel_values = im.getpixel((x,y))
                                sigma += pixel_values[args.c]

                mean = int(sigma/16**2)

                alpha = im.getpixel((s_index_x, s_index_y))[0] - mean
                beta = im.getpixel((s_index_x, s_index_y + 1))[0] - mean

                print mean
                print(s_index_x, s_index_y)
                print im.getpixel((s_index_x, s_index_y)),im.getpixel((s_index_x, s_index_y + 1))

                c = chr((alpha * 16) + beta)
                print(c, end="")

                i += 1

if (args.m is not None):
    msg = open(args.m,'rb').read()
    encode_message(msg)
    im.save(args.f)
else:
    print decode_message()