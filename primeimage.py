# written 3 oct 18 by William Matthews
# inspired by the Trinity Hall Prime

from scipy import misc
import numpy as np
import time

#import matplotlib.pyplot as plt

import getopt
import sys



def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite


def is_prime(n, _precision_for_huge_n=16):
    """Checks if n is prime using the Miller-Rabin primality test, code from rosettacode"""
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 

def primecheckrange(startnum,numtotest=10000):
    """Given a starting number (the image), increments image until a prime
    is found or number of tests is greater than numtotest.
    Returns the prime if a prime is found, otherwise returns 0"""

    i = 1
    # force image to be odd
    if startnum % 2 == 0:
        startnum += 1

    # test odd numbers in the range specified
    for n in range(startnum,startnum+numtotest,2):
        print("Candidate", i , end="", flush=True)
        result = is_prime(n)
        i += 1
        print("checked:",result)
        if result:
            return n
    else:
        return int()


def to_binary(img, lower, upper):
    """Converts numpy ndarray from integer to Boolean
    This is useful as a greyscale can be fed in and a binary image returned"""
    return (lower< img) & (img < upper)


def to_imagenum(pixel, white=1, black=8):
    """Converts Boolean pixel to an integer"""
    if pixel:
        return black
    else:
        return white


def get_image(path,size_y=25,size_x=50,autoaspect=True):
    """Given the path of an image, function reads image, resizes, and returns a binary image with dimensions in a tuple"""
    # read image
    f = misc.imread(path, mode='L') # read as greyscale
    
    if autoaspect:
        # get aspect ratio, y/x
        ar = len(f)/len(f[0])
        pass # feature not yet implemented

    f = misc.imresize(f,(size_y, size_x),interp='bilinear') # resize as a 25 x 50
    bw = to_binary(f,150,210)
    return (bw,(size_y, size_x))


def get_imagenum(binimage):
    """get_imagenum takes a binary image (numpy ndarray of Bool) and converts it to a single integer of numbers as specified in to_imagenum"""

    # concat list
    imgnumlist = []
    for row in binimage:
        for element in row:
            imgnumlist.append(to_imagenum(element))
    s = ''.join(map(str,imgnumlist))
    print("Image is", len(s) ," digits long")
    return int(s)


def get_path():
    root = tk.Tk()
    root.withdraw()
    return askopenfilename(parent=root,title="Please Select Image File")


def univcrest():
    """Returns a constant, the University College Crest number (1249 digits long - year of founding)"""
    crest = """11111111111111111111111188111111111111111111111111
        11111111111111111111881888818811111111111111111111
        11111111111111111111118888881111111111111111111111
        11111888811111111111118888881118888111111111111111
        11111188881111111111118888881111888811111111111111
        11111188888881111111118888881111888888811111111111
        11111118811188881111118888881111881118888111111111
        11111111188888888881118888881111118888888888111111
        11111111111888111881118888881111111188811188111111
        11111111111111111111118888881111111111111111111111
        11188111111111111111118888881111111111111111188111
        11118888888888888888888888888888888888888888881111
        11888888888888888888888888888888888888888888888811
        11118888888888888888888888888888888888888888881111
        11188111111111111111118888881111111111111111188111
        11111111111111111111118888881111111111111111111111
        11111188881111111111118888881118888111111111111111
        11111118888111111111118888881111888811111111111111
        11111118888888111111118888881111888888811111111111
        11111118811188881111118888881111881118888111111111
        11111111188888888881118888881111118888888888111111
        11111111111888111881118888881111111188811188111111
        11111111111111111111118888881111111111111111111111
        11111111111111111111881888818811111111111111111111
        1111111111111111111111118811111111111111111111111"""

    # clean and return
    crest = crest.replace('\n','')
    crest = crest.replace(' ','')
    return (int(crest),(25,50))

#######################################################



# build list of prime numbers for primality test to use
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]



def main(argv):
    
    # parse arguments
    useuniv = False
    path = ""

    try:
        opts, args = getopt.getopt(argv, "hui:", ["univ","infile="])
    except getopt.getoptGetoptError:
        print("primeimage.py -h -i <inputfile -u")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("\nprimeimage.py -h -i <inputfile> -u \n\n -h :  prints help \n -i : input file \n -u : load University College crest")
            sys.exit()
        elif opt in ("-u","--univ"):
            useuniv = True
        elif opt in ("-i","--infile"):
            path = arg


    if useuniv:
        imagenum, size = univcrest()
    else:
        # if we have a path to work with
        if path:
            bimage, size = get_image(path,size_x=25,size_y=50)
            imagenum = get_imagenum(bimage)
        else:
            print("No Image Specified!")
            imagenum = 0

    # start the clock
    t0 = time.time()

    # if we have an image number - try and obtain a prime, otherwise maybeprime = 0
    if imagenum:
        maybeprime = primecheckrange(imagenum)
    else:
        maybeprime = 0

    # stop the clock
    t1 = time.time()

    # if we have a prime (maybeprime != 0), write it to disk
    if maybeprime:
        try:
            fh = open("primeout.txt","w")
            try:
                # split prime by row and save to file
                sy, sx = size
                for i in range(sy):
                    fh.write(str(maybeprime)[(i*sx):((i+1)*sx)] + "\n")
            finally:
                fh.close()
        except IOError:
            print("Error, Can't find file or write data")
    else:
        print("Prime Not Found, Expand search and try again")

    print("Elapsed Time:", t1-t0 ,"seconds")



if __name__ == "__main__":
    main(sys.argv[1:])
