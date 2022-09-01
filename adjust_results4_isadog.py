#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog_hints.py
#                                                                             
# PROGRAMMER: OBAFEMI OLUWADOLAPO SUCCESS
# DATE CREATED: 30TH AUGUST,2022       
# REVISED DATE: 30TH AUGUST,2022    

def adjust_results4_isadog(results_dic, dogfile):
    #dogfile = dognames.txt
    # OPening an empty dictionary
    dognames_dic = dict()

    # Reads in dognames from file, 1 name per line & automatically closes file
    with open(dogfile, "r") as infile:
        # Reads in dognames from first line in file
        line = infile.readline()

        # Iterates each line in file until reaching the end by iterating line and adding dognames to dognames_dic with while loop
        while line != "":

            # Process line by striping newline from line
            line = line.rstrip()
            
            line = line.replace('\n','')
            
            # adds dogname(line) to dogsnames_dic if it doesn't already exist in the dogsnames_dic dictionary
            if line not in dognames_dic:
                dognames_dic[line] = 1
                #dognames_dic[line].replace('\n', '')

            # Reads in next line in file to be processed with while loop if this line isn't empty
            line = infile.readline()
    #print(dognames_dic)       
    for key in results_dic:
                # Comparing pet name label with the dog names in the dognames_dic
                # This is for check for the similar names in pet name label found in Dog names Dictionary
                # Pet Image Label IS of Dog (e.g. found in dognames_dic)
                if results_dic[key][0] in dognames_dic:
                    
                    # Comparing Classifier label with the dog names in the dognames_dic
                    # This is for check for the similar names in pet name label in alignment with the image of dog in Classifier label found in Dog names Dictionary
                    # Classifier Label IS image of Dog (e.g. found in dognames_dic) appends (1, 1) because both labels are dogs
                    if results_dic[key][1] in dognames_dic:
                        results_dic[key].extend((1, 1))

                        # Classifier Label IS NOT image of dog (e.g. NOT in dognames_dic)
                        # appends (1,0) because only pet label is a dog
                    else:
                        results_dic[key].extend((1, 0))

                        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
                else:

                        # Classifier Label IS image of Dog (e.g. found in dognames_dic) appends (0, 1)because only Classifier label is a dog
                        if results_dic[key][1] in dognames_dic:
                            results_dic[key].extend((0, 1))

                            # Classifier Label IS NOT image of Dog (e.g. NOT in dognames_dic) appends (0, 0) because both labels aren't dogs
                        else:
                            results_dic[key].extend((0, 0))
    print(results_dic)
    #print(adjust_results4_isadog(results_dic, in_arg.dogfile))
