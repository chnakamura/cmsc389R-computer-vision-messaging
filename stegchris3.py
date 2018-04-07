from PIL import Image
import time, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="message to encode")
parser.add_argument("-f", help="image path")
args = parser.parse_args()

if args.f is None:
    exit("Need to specify image path!")

im = Image.open(args.f, 'r')
width,height = im.size

def encode_message(msg = "Hello World!"):

    i = 0

    for x in xrange(0,width,4):
        for y in xrange(0,height,4):
            print(x,y)
            if i < len(msg):
                r,g,b,a = im.getpixel((x,y))
                im.putpixel((x,y),(ord(msg[i]),g,b,a))
            else:
                im.putpixel((x,y),(69,69,69,69))
                return
            i += 1

def decode_message():

    msg = ""

    for x in range(0,width,4):
        for y in range(0,height,4):

            r,g,b,a = im.getpixel((x,y))

            if (r,g,b,a) == (69,69,69,69):
                return msg
            else:
                msg += chr(r)

            y += 10

        x +=10
if (args.m is not None):
    msg = open(args.m,'rb').read()
    encode_message(msg)
    im.save(args.f)
else:
    print decode_message()