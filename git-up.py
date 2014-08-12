#!/usr/bin/env python
# -*- coding: utf-8 -*-

from git import *

def git_up():
    git_fetch()
    git_subtree_merge("scripts", "scripts")

    branches = ["master"]
    previous_branch = None
    for branch in branches:
        git("checkout", branch)
        git("merge origin/%s" % branch)
        if previous_branch:
            git("merge", previous_branch)
        previous_branch = branch


if __name__ == '__main__':
    git_up()
