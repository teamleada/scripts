#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def prompt_multiple_lines(message):
    print prompt + " (press enter twice to terminate)\n"
    lines = []
    while lines[-2:] != ["", ""]:
        lines.append(raw_input())
    return "\n".join(lines).strip()

def call(popenargs, input=None, requested_return=None, check_return_code=False, **kwargs):
    if "stdin" not in kwargs and input != None:
        kwargs["stdin"] = subprocess.PIPE

    if "stdout" not in kwargs and requested_return == "stdout":
        kwargs["stdout"] = subprocess.PIPE
    elif "stderr" not in kwargs and requested_return == "stderr":
        kwargs["stderr"] = subprocess.PIPE

    p = subprocess.Popen(popenargs, **kwargs)
    stdout, stderr = p.communicate(input)
    output = p.returncode
    if requested_return == "stdout":
        output = stdout
    elif requested_return == "stderr":
        output = stderr
    elif requested_return == "code":
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

def current_branch():
    for branch in git("branch").split("\n"):
        if branch.startswith("*"):
            return branch[2:]
    raise RuntimeError("No current branch")

def git_commit(message):
    return git("commit -am " + message)

def git_fetch():
    return git("fetch")

def git_subtree_merge(subtree, prefix):
    git_subtree_pull(subtree, prefix)
    git_subtree_push(subtree, prefix)

def git_subtree_pull(subtree, prefix):
    default_pull_message = "'[%s subtree] Merging %s into %s'" % (subtree, subtree, current_branch())
    git("subtree pull", "--prefix=%s" % prefix, "--squash", "-m", default_pull_message, subtree, "master")

def git_subtree_push(subtree, prefix):
    git("subtree push", "--prefix=%s" % prefix, subtree, "master")

def git_up():
    git_fetch()
    git_subtree_pull("scripts", "scripts")
    git_subtree_pull("primary", "app/assets/stylesheets/primary")

    branches = ["master"]
    previous_branch = None
    for branch in branches:
        git("checkout", branch)
        git("merge origin/%s" % branch)
        if previous_branch:
            git("merge", previous_branch)
        previous_branch = branch

