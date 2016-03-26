#!/usr/bin/python
#-*- coding: utf-8 -*-

def function(mag, matches, peer):
	message = """
	A telegram bot written in python
	Made by @This_Is_Amir
	
	"""
	return message

plugin = {
	'name': "About",
	'tag': "about",
	'patterns': ["^/about$"],
	'function': function,
	'elevated': False,
	'usage' : "/about",
	'desc' : "Shows the about text"
	}

