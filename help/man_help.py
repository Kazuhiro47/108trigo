#!/usr/bin/python3
# coding=UTF-8

from sys import stdout

def man():
    help_file = open("man", 'r')
    stdout.write(help_file.read())
