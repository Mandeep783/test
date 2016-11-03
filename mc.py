# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 12:34:41 2016

@author: Mandeep Chaudhary

This script is python 2.7 compatible
In this script m_c() that takes a plaintext file as an argument 
and downloads all images, storing them on the local hard disk or at desired location. 
"""

#importing urllib for performing url operations
import urllib 



# creating a function m_c  which takes one argument i.e. filename
def m_c(filename_1):
    
    try :
    
      file_read = open (filename_1,'r') # open the file in the read mode
      
      counter = 0  # initialising the counter for saving the pictures   
      
      for line in file_read: # using for loop to read each of the line
          
          counter = counter + 1 # incrementing the counter
          
          #print line  # for testing purposes
          
          urllib.urlretrieve(line,'file_%d.jpg' %(counter)) # saving the image from url onto the hard disk
         
          
          # urllib.urlretrieve(line1,'C:/Users/Mandeep/Desktop/file_%d.jpg' %(counter)) # for saving the file at a desired location
          
    except Exception, e: 
         print e # This will print out the error such as IOError / ValueError etc.          
