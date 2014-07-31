#!/usr/bin/env python

import subprocess

def git(space_delimited_args):
    print "Running git %s" % space_delimited_args
    return subprocess.Popen("git " + space_delimited_args)

def git_commit(message):
    return git("commit -am " + message)

git_commit("test")
