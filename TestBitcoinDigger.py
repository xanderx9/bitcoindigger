# https://en.wikipedia.org/wiki/Bloom_filter
# Bloom filter module for private key search accelerator for Bitcoin Addresses
# To test the functionality of the script Bloom filter module is OFF !!!

import Chmod
import SpeedUP
import BloomFilter
from bitcoin import *
import os

counter = 0

while counter < 1:

    priv =  random_key()
    pub = privtopub(priv)
    addr = pubtoaddr(pub)[:-24]

    #searches file for address match if the priv key generated matchs any address in the Address.txt it will print it and auto save it
    searchfile = open("TestAddress.txt","r")

    for line in searchfile:
        if addr in line:
                
                print("PrivKey = "+priv+" - Address = " + addr + "\n")
                # Autosave Private Key to file "TestKeyFound.txt"
                f = open("TestKeyFound.txt", 'a')
                f.write("PrivKey = " + priv + " - Address = " + addr + "\n")
                f.close()


