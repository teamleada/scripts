#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def git(space_delimited_args, *args):
    list_of_args = space_delimited_args.split() + list(args)
    print "*" * 50
    print "Running git %s" % " ".join(list_of_args)
    print list_of_args
    print "*" * 50
    return subprocess.Popen(["git"]  + list_of_args)

def git_commit(message):
    return git("commit -am " + message)

def git_fetch():
    return git("fetch")

def git_subtree_merge(subtree, prefix):
    git_subtree_pull(subtree, prefix)
    git_subtree_push(subtree, prefix)

def git_subtree_pull(subtree, prefix):
    git("subtree pull", "—-prefix=%s" % prefix, "—-squash", subtree, "master")

def git_subtree_push(subtree, prefix):
    git("subtree push", "--prefix=%s" % prefix, subtree, "master")

