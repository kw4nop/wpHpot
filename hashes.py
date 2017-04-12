#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
import os
import hashlib
import traceback
import itertools


def generate_list(directory,verbose=1):

	SHAhash = ""
	if not os.path.exists (directory):
		return -1
	try:
		f = open('hashes.txt', 'r+')
    		for root, dirs, files in os.walk(directory):
      			for names in files:
        			
				filepath = os.path.join(root,names)
        			try:
          				f1 = open(filepath, 'rb')

        			except:
          				# You can't open the file for some reason
          				f1.close()	
          				continue

	  			# Read file in as little chunks
  	  			buf = f1.read(4096)
	  			if not buf : break
	  			SHAhash = hashlib.sha1(buf).hexdigest()
				if verbose == 1:
					f.write ("%s %s \n" % (filepath,SHAhash))
        			
				f1.close()
		f.close()

  	except:
    		# Print the stack traceback
    		traceback.print_exc()
    		return -2

	

def check_integrity(directory,verbose=1):

	SHAhash = ""
	actual = {}
	if not os.path.exists (directory):
		return -1
	try:
    		for root, dirs, files in os.walk(directory):
      			for names in files:
        			
				filepath = os.path.join(root,names)
        			try:
          				f1 = open(filepath, 'rb')

        			except:
          				# You can't open the file for some reason
          				f1.close()
					print "cant open"	
          				continue

	  			# Read file in as little chunks
  	  			buf = f1.read(4096)
	  			if not buf : break
	  			SHAhash=hashlib.sha1(buf).hexdigest()
				if verbose == 1:
					actual.update ({filepath:SHAhash})

				f1.close()
  	except:
    		# Print the stack traceback
    		traceback.print_exc()
    		return -2

	f = open('hashes.txt', 'r+')
	lines = f.read().split()
	dictionary = dict(itertools.izip_longest(*[iter(lines)] * 2, fillvalue=""))

	diff = set(actual.iteritems()) - set(dictionary.iteritems())

	return diff



if __name__ == "__main__":
	exit(main())
	
