#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def call(popenargs, input=None, requested_return=None, check_return_code=False, **kwargs):
    p = subprocess.Popen(popenargs, **kwargs)
    stdout, stderr = p.communicate(input)
    output = p.returncode
    return output

def check_call(popenargs, input=None, requested_return="", **kwargs):
    return call(popenargs, input=input, requested_return=requested_return, check_return_code=True, **kwargs)

def check_call_and_get_stdout_and_stderr(popenargs, **kwargs):
    return check_call(popenargs, requested_return="stdout", stderr=subprocess.STDOUT, **kwargs)

def git(space_delimited_args, *args):
    list_of_args = space_delimited_args.split() + list(args)
    print "Running git %s" % " ".join(list_of_args)
    return check_call_and_get_stdout_and_stderr(["git"] + list_of_args)

def git_commit(message):
    return git("commit -am " + message)

def git_fetch():
    return git("fetch")

def git_subtree_merge(subtree, prefix):
    git_subtree_pull(subtree, prefix)
    git_subtree_push(subtree, prefix)

def git_subtree_pull(subtree, prefix):
    git("subtree pull", "--prefix=%s" % prefix, "--squash", subtree, "master")

def git_subtree_push(subtree, prefix):
    git("subtree push", "--prefix=%s" % prefix, subtree, "master")

