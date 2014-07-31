#!/usr/bin/env python

import subprocess

def git(space_delimited_args):
    print "Running git %s" % space_delimited_args
    list_of_args = space_delimited_args.split()
    return subprocess.Popen(["git"]  + list_of_args)

def git_commit(message):
    return git("commit -am " + message)
