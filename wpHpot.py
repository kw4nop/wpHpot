#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys

from hashes import generate_list, check_integrity



def main():

    try:
    	#generate_list(sys.argv[1])
	print  check_integrity(sys.argv[1])
	
    except:
        print ('Usage: wpHpot <option>\n\n'\
		'available options:\n'\
		'+ generate_hashes\n'\
		'+ check_integrity\n')
        sys.exit(2)




if __name__ == "__main__":
	exit(main())
	
