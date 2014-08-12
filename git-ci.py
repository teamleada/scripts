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

    # Git up will merge in master and any subtree changes
    # We then want to push your branch to origin HEAD
    # Open a pull request with your summary and close any issues.
    # Dump you back on master with all the updated changes.
    git("push origin HEAD")

if __name__ == '__main__':
    git_ci()

