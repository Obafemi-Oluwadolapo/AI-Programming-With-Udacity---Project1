#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: OBAFEMI OLUWADOLAPO SUCCESS
# DATE CREATED: 27TH AUGUST, 2022        
# REVISED DATE: 28TH AUGUST, 2022
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from get_input_args import get_input_args

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    file = get_input_args()
    filename_list = listdir(file.dir)
    
    # Print 10 of the filenames from folder pet_images/
    #print("\nPrints 40 filenames from folder pet_images/")
    #for idx in range(0, 40, 1):
    #    print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )
    
   
    values = []
    for index in range(0,len(filename_list), 1):
        # Iterating over each image of every pet
        pet_image = filename_list[index]
        
        # the lowercase of the names of the pet images (the names are in string form)
        pet_image_lowercase = pet_image.lower()
        
        # Splitting the string by "_"
        pet_image_words = pet_image_lowercase.split("_")
        
        pet_name = ""
        
        # Iterating through the words in pet images words to remove non alphabets using .isalpha() and the words together
        for word in pet_image_words:
            if word.isalpha():
                pet_name +=  word + " "
                
                # Skipping words that starts with '.'
                if word.startswith('.'):
                    continue
        pet_name = pet_name.strip()
        #print(f"\nFilename {pet_image}, Label= {pet_name}")
        values.append(pet_name)
    #print(values)
    #print(filename_list)
    
    results_dic = {}
    for index in range(0, len(filename_list), 1):
        if filename_list[index] not in results_dic:
             results_dic[filename_list[index]] = [values[index]]
        else:
             print("** Warning: Key=", filename_list[index], 
                   "already exists in results_dic with value =", 
                   results_dic[filename_list[index]])

    #Iterating through a dictionary printing all keys & their associated values
    #print("\nPrinting all key-value pairs in dictionary results_dic:")
    #for key in results_dic:
        #print("Filename=", key, "   Pet Label=", results_dic[key][0])    
   
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
