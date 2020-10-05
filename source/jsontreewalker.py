#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# SCRIPT-NAME ... jsontreewalker.py
# AUTHOR ........ marcus.trommen@gmx.net
# CREATED ....... 2020-08-31
# -----------------------------------------------------------------------------
# PURPOSE
# Script takes as command line paramter a path-name.
#
# Usage: ./jsontreewalker.py path-name
#
# collects all directory names, file and link names given in this path location
# and walks along recursively the whole substructure
# ------------------------------------------

from dirtreewalker import DirTreeWalker
import os
import sys
import json


class JsonTreeWalker(DirTreeWalker):
	"""
	Collects all directory names, file and link names given in this path 
	location and walks along recursively the whole substructure.
	For each directory entry element type (e.g. file, dirctory, link, mount) a
	callback method is called. In the base class all callback methods are 
	defined as abtract.
	"""


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
		if direntry.endswith(".json") :
			self.handle_json_file(directory, fully_qualified_entry_name)


	# ------------------------------------------
	def handle_json_file(self, directory, json_file):
		json_dict = {}
		
		with open(json_file, 'r') as fileObject:
			json_text = fileObject.read()
		
		json_dict = json.loads(json_text)
		
		
		json_dict["file_fqn"] = os.path.join(directory, json_dict["file"])
		self.data[json_dict["id"]] = json_dict


# ------------------------------------------
def handle_cli():
	# parse command line parameters
	# retrieve fully qualified path-name
	USAGE = "Usage: {} path-name".format(sys.argv[0])
	
	if len(sys.argv) < 2:
		sys.exit(USAGE)
	
	parameter = sys.argv[1]
	path = os.path.realpath(parameter)
	if not os.path.isdir(path):
		print("ERROR: parameter " + parameter + " is not a directory!")
		sys.exit(USAGE)
	
	return path


# ------------------------------------------
def dump_data_to_json_file(file_name, data):
	#  write json file into same path of this script
	outFileName = os.path.join(get_script_path(), file_name)
	
	with open(outFileName, 'w') as fileObject:
		fileObject.write(json.dumps(data, indent=4, sort_keys=True))


# ------------------------------------------
def get_script_path():
	outPath = os.path.realpath(__file__)
	return os.path.dirname(outPath)


# ------------------------------------------
if __name__ == '__main__':
	path = handle_cli()
	
	handler = JsonTreeWalker()
	handler.parse_dir(directory=path)
	data_dict = handler.getData()
	
	dump_data_to_json_file(file_name="bla.json", data=data_dict)
	exit(0)
