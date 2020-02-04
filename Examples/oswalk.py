# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:03:37 2020

@author: trellis
"""
#
import os
#root="Kritik"
#for path,directories,files in os.walk(root,topdown=True):
#    print(path)
#    print(files)
#    print(directories)
#    input()
#    
    
#root="music"
#for path,directories,files in os.walk(root,topdown=True):
#    if files:
##        print(path)
#        first_split=os.path.split(path)
##        print(first_split)
#        second_split=os.path.split(first_split[0])
##        print(second_split)
#     print(files)
#     

import fnmatch
def find_albums(root,artist_name):
    for path,directories,files in os.walk(root):
        for artist in fnmatch.filter(directories,artist_name):
            subdir=os.path.join(path,artist)
            for album_path,albums,_ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path,album),album
def find_song(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song
        
album_list=find_albums("music","Be Bop Deluxe")
songs=find_song(album_list)

for s in songs:
    print(s)    
    
    
    

