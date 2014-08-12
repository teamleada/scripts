#!/usr/bin/env python
# -*- coding: utf-8 -*-

from git import *

ENGINEER_GITHUB_USERNAMES = [
    "negativetwelve",
    "tristantao",
    "brianliou",
]

def git_ci():
    git_up()

    initial_branch = current_branch()

    commit_description = prompt_multiple_lines("Enter a commit description. The frist line will be the summary.")
    commit_description_by_line = commit_description.split("\n")
    summary = commit_description_by_line[0]

    git("checkout", "master")
    git("merge --squash", initial_branch)

    git_subtree_push("scripts", "scripts")
    git_subtree_push("primary", "app/assets/stylesheets/primary")

    git("push origin HEAD")

if __name__ == '__main__':
    git_ci()

