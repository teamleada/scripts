#!/usr/bin/env python
# -*- coding: utf-8 -*-

from git import *

def git_ci():
    git_fetch()
    git_subtree_push("scripts", "scripts")
    git_subtree_push("primary", "app/assets/stylesheets/primary")

    branches = ["master"]
    previous_branch = None
    for branch in branches:
        git("checkout", branch)
        git("merge origin/%s" % branch)
        if previous_branch:
            git("merge", previous_branch)
        previous_branch = branch

if __name__ == '__main__':
    git_ci()

