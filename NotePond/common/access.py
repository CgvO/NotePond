from django.shortcuts import render
from django.contrib import messages
from common.models import Note, Tag, Course


def download(file_tag):
    '''parameter passed in is the file_tag or database locationof file
       function grabs file from database and returns it to user '''
    
    

    
def get_file_metadata(file_tag): '''Retrieves file metadata associated with desired file from the database '''

def upload(document):
    '''parameter passed in is the document the user uploaded, this function should safely store document(s) to the database, return could be bool based on success'''

'''def find_files(search_results) could be  a function defined here or it can be called from filter.py'''

