#!/usr/bin/env python
# -*- coding: utf-8 -*-

from git import *

def hub(space_delimited_args, *args):
    list_of_args = space_delimited_args.split() + list(args)
    print "Running hub %s" % " ".join(list_of_args)
    return check_call_and_get_stdout_and_stderr(["hub"] + list_of_args)

def pull_request():
    

