# PrimeImage
Find prime numbers in the shape of binary images

## It does what now?
PrimeImage produces prime numbers to appear like arbitary (binary) images - for example this smiley face!
```
11111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111
11111111111111111881111111111188811111111111111111
11111111111111181118811111111811181111111111111111
11111111111111181111811111118111118111111111111111
11111111111111181111811111111811118111111111111111
11111111111111118888111111111888881111111111111111
11111111111111111111111111111111111111111111111111
11111111188111111111111111111111111111181111111111
11111111818111111111111111111111111111818111111111
11111111811811111111111111111111111118118111111111
11111111181881111111111111111111111118118111111111
11111111188188111111111111111111111881181111111111
11111111118811881111111111111111118111811111111111
11111111111181118881111111111118811188111111111111
11111111111118881111888888888811118811111111111111
11111111111111118888111111111188811111111111111111
11111111111111111111188888881111111111111111111111
11111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111112251
```

In its current state the last few digits are mutated until a prime is found.
The digits at the end are currently incremented by two (maintaining the odd property of the number),
and a primality test is run on each number.


## Usage
PrimeImage was written as a Python 3 project, 
for Python 2 I have not tested and cannot guarantee it'll work, due to the use of iterators.

To immediately jump in and have fun, run from terminal `python3 primeimage -u`, which will load a test image
(my College's crest) and generate a prime that looks like it (should occur on the 111th candiate!).

To load an arbitary image (at the moment the image should be square!), run `python3 -i ~/path/to/image`.
Most common formats (.png, .jpg, .bmp etc) are supported.

Help can be loaded by using the `-h` flag.


## Limitations (and todos!)
1. For the moment the images are small, on the order of 25 x 50 pixels.
   + if you insist on a larger image you can change the `size_x` and `size_y` on the function call on line 192. 
1. The y dimension has a lower spatial resolution (half of x dimension) due to the use of monospaced integers.
1. Prime number images are only binary (for now).
1. Images *should be square*. In an upcoming version adaptive sizing will be avaliable.
   + for now - if you really do insist on an arbitary
      dimensioned image you can change the `size_x` and `size_y` on the function call on line 192. 
      Just be wary that `size_y` should be half what you expect, owing to monospaced numbers being twice high as wide.


## Installation
PrimeImage needs a version of Python 3 installed (ver > 3.5).

PrimeImage needs the following packages:

1. scipy
1. numpy
1. matplotlib (in future generations)
1. time

## Theory
Please standby... will add in following few days.
