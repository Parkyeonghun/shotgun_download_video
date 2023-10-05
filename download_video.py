#!/usr/bin/env python3

import os
import sys
import shutil
import logging as logger

import shotgun_api3

from handler import ShotgunAction

class DownloadVideo:
    def __init__(self):
        self.protocol_url = sys.argv[1]
        self.sa = ShotgunAction(self.protocol_url)

        SERVER_PATH = 'https://westrnd2.shotgrid.autodesk.com'
        SCRIPT_NAME = 'download_video'
        SCRIPT_KEY = '^trurx1vahkkezwyDotlzxvbs'

        self.sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
        
        self.filter = self.sa.selected_ids_filter
        self.entity_type = self.sa.entity_type
        print(self.filter)
        print(self.entity_type)

        for one_filter in self.filter:
            self.result_file = self.sg.find_one('Version', [one_filter], ['sg_path_to_movie', 'sg_uploaded_movie'])
            self.path_to_movie = self.result_file['sg_path_to_movie']
            self.local_file_path = "/westworld/show/%s/product" % self.sa.project['name']
            
            if self.result_file['sg_uploaded_movie'] == None:
                print('"sg_uploaded_movie" is None')

            else:
                self.file_path=self.local_file_path+"/%s" % self.result_file['sg_uploaded_movie']['name']

                if os.path.isfile(self.path_to_movie):
                    self.download_file_from_path()
                else:
                    self.download_attachment()


    def download_attachment(self):
        if not os.path.isdir(self.local_file_path):
            os.makedirs(self.local_file_path)
        if not os.path.isfile(self.file_path):
            self.sg.download_attachment(self.result_file['sg_uploaded_movie'], 
                                        file_path=self.file_path)
            print('download_attachment == ', self.result_file['sg_uploaded_movie']['name'])
        else:
            print('file exists')

    def download_file_from_path(self):
        if not os.path.isdir(self.local_file_path):
            os.makedirs(self.local_file_path)
        if not os.path.isfile(self.file_path):
            shutil.copyfile(self.path_to_movie, self.file_path)
            print('download_file_from_path ==', self.result_file['sg_uploaded_movie']['name'])
        else:
            print('file exists')

# ----------------------------------------------
# Main Block
# ----------------------------------------------
if __name__ == "__main__":
    dv = DownloadVideo()
