#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
OS-independent commands for handling files
'''

import os
import shutil
from glob import glob


def create_empty_file(filepath):
    ''' Create empty file at filepath '''
    open(filepath, 'w').close()


def create_stream_file(plugin_path, filepath):
    ''' Create stream file with plugin_path at filepath '''
    with open(filepath, 'w') as f:
        f.write(plugin_path)


def softlink_file(src, dst):
    ''' Copy file at src to dst '''
    # Can only symlink on unix, just copy file
    shutil.copyfile(src, dst)


def softlink_files_in_dir(src_dir, dst_dir):
    ''' Symlink all files in src_dir using wildcard to dst_dir '''
    # Can only symlink on unix, just copy files
    for fname in os.listdir(src_dir):
        shutil.copyfile(os.path.join(src_dir, fname), os.path.join(dst_dir, fname))


def mkdir(dir_path):
    ''' Make directory at dir_path '''
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def mv_with_type(title_path, filetype, title_dst):
    ''' Move files with wildcard between title_path & filetype to title_dst '''
    for path in glob('{0}*{1}'.format(title_path, filetype)):
        os.rename(path, title_dst + filetype)


def rm_strm_in_dir(dir_path):
    ''' Remove all stream files in dir '''
    for filepath in glob(os.path.join(dir_path, '*.strm')):
        os.remove(filepath)


def rm_with_wildcard(title_path):
    ''' removes all files starting with title_path using wildcard '''
    for filepath in glob(title_path + '*'):
        os.remove(filepath)


def remove_dir(dir_path):
    ''' removes directory at dir_path '''
    shutil.rmtree(dir_path)
