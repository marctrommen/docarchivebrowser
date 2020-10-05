#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# SCRIPT-NAME ... dirtreewalker.py
# AUTHOR ........ marcus.trommen@gmx.net
# CREATED ....... 2020-07-28
# -----------------------------------------------------------------------------
# PURPOSE
# Script takes as command line paramter a path-name.
#
# Usage: ./dirtreewalker.py path-name
#
# collects all directory names, file and link names given in this path location
# and walks along recursively the whole substructure
# ------------------------------------------

from abc import ABC, abstractmethod
import os


class DirTreeWalker(ABC):
	"""
	Collects all directory names, file and link names given in this path 
	location and walks along recursively the whole substructure.
	For each directory entry element type (e.g. file, dirctory, link, mount) a
	callback method is called. In the base class all callback methods are 
	defined as abtract.
	"""

	def __init__(self, data = None):
		"""
		Initializes the class instance
		:param dict data: data structure for optional collecting data while 
			traversing the directory tree
		:return: nothing
		:raises AttributeError: if data is none or not of type dictionary
		"""
		if data == None:
			self.data = {}
		else:
			if data == None:
				raise AttributeError("ERROR: Data is None!")
	
			if isinstance(data, dict):
				raise AttributeError("ERROR: Data is not of type dictionary!")
			
			self.data = data


	# ------------------------------------------
	def getData(self):
		"""
		return dict data: data structure for optional collecting data while 
			traversing the directory tree
		"""
		return self.data
	
	
	# ------------------------------------------
	def parse_dir(self, directory):
		"""
		Entry point for parsing a whole directory tree. Walks over all entries in
		a diectory and calls for each entry type (e.g. file, link, mount or 
		directory) a callback function.
	
		:param os.path directory: retrieve all directory entries of this path
		:return: nothing
		:raises AttributeError: if path is not of type directory or not existing
		"""
		if not os.path.isdir(directory):
			raise AttributeError("ERROR: Value for 'directory' is not a directory or does not exist!")
	
		entries = os.listdir(directory)
		for direntry in entries:
			# get fully qualified entry name
			fqen = os.path.join(directory, direntry)
		
			if os.path.isfile(fqen):
				self.handle_file(direntry, directory, fully_qualified_entry_name=fqen)
			elif os.path.isdir(fqen):
				self.handle_dir(direntry, directory, fully_qualified_entry_name=fqen)
			elif os.path.islink(fqen):
				self.handle_link(direntry, directory, fully_qualified_entry_name=fqen)
			elif os.path.ismount(fqen):
				self.handle_mount(direntry, directory, fully_qualified_entry_name=fqen)
			else :
				print("something totally different:", fqen)


	# ------------------------------------------
	def handle_file(self, direntry, directory, fully_qualified_entry_name):
		"""
		Callback function for parse_dir(). It gets called in case 'direntry' is of
		type file.
	
		:param str direntry: name of the file without path
		:param os.path directory: basepath of file
		:param os.path fully_qualified_entry_name: fully qualified pathname of the 
			file
		:return: nothing
		"""
		print("is file:", fully_qualified_entry_name)


	# ------------------------------------------
	def	handle_dir(self, direntry, directory, fully_qualified_entry_name):
		"""
		Callback function for parse_dir(). It gets called in case 'direntry' is of
		type directory. In case of READ access to the directory it recursively
		calls parse_dir().
	
		:param str direntry: name of the directory without (base-)path
		:param os.path directory: basepath of directory
		:param os.path fully_qualified_entry_name: fully qualified pathname of the 
			directory
		:return: nothing
		"""
		# check if read access on directory exists
		if os.access(fully_qualified_entry_name, os.R_OK):
			# recurse into sub-directory
			self.parse_dir(fully_qualified_entry_name)


	# ------------------------------------------
	def handle_link(self, direntry, directory, fully_qualified_entry_name):
		print("is Link:", fully_qualified_entry_name)


	# ------------------------------------------
	def handle_mount(self, direntry, directory, fully_qualified_entry_name):
		print("is Mount:", fully_qualified_entry_name)
