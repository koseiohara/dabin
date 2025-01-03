#
# Sample program to use dabin.f90 and fileio.py
#
# Provided by Kosei Ohara
#

import numpy as np

from fileio import fileio

nx = 288
ny = 145
nz = 45
shape = [nx,ny,nz]
kind = 4

nt = 10

ifile = 'input.bin'
ofile = 'output.bin'

# Input File
iclass = fileio(filename=ifile          , \
                action  ='read'         , \
                shape   =shape          , \
                kind    =kind           , \
                record  =1              , \
                recstep =1              , \
                endian  ='little_endian', \
                order   ='C'              )

# Output File
oclass = fileio(filename=ofile          , \
                action  ='write'        , \
                shape   =shape          , \
                kind    =kind           , \
                record  =1              , \
                recstep =1              , \
                endian  ='little_endian', \
                order   ='C'              )

work = np.empty(shape)
# Read a file and write the data to another file
for t in range(nt):
    work = iclass.fread()
    oclass.fwrite(work)

iclass.close()
oclass.close()

