"""
ssh-medic.py

This module provides a command-line interface (CLI) tool to ensure that SSH directories and files
have the correct permissions. It uses the Click library to define commands and options.

Commands:
- check: Checks the permissions of the SSH directory and its files, and reports any discrepancies.

Usage:
$ python ssh-medic.py check
"""

import click
import os

# Define context settings for Click, including help option names
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help", "help"])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """
    Ensure SSH directories and files have correct permissions:

    \b
    $HOME/.ssh      -> 700
    authorized_keys -> 644
    known_hosts     -> 644
    config          -> 644
    *.pub keys      -> 644
    All private key -> 600
    """
    return

@main.command()
def check():
    """
    Check the permissions of the SSH directory and its files.
    Reports any files that do not have the expected permissions.
    """
    ssh_dir = os.path.expanduser("~/.ssh")
    absolute_path = os.path.abspath(ssh_dir)
    files = [ssh_dir] + os.listdir(ssh_dir)

    # Expected permissions
    public_permissions = "644"
    private_permissions = "600"
    expected = {
        ssh_dir: "700",
        "authorized_keys": "644",
        "known_hosts": "644",
        "config": "644",
        ".ssh": "700",
    }

    for _file in files:
        # Public keys can use the .pub suffix
        if _file.endswith(".pub"):
            expected[_file] = public_permissions

        # Stat the file and get the octal permissions
        file_stat = os.stat(os.path.join(ssh_dir, _file))
        permissions = oct(file_stat.st_mode)[-3:]

        try:
            expected_permissions = expected[_file]
        except KeyError:
            # If the file doesn't exist in the expected dictionary, consider it as a private key
            expected_permissions = private_permissions

        # Only report if there are unexpected permissions
        if expected_permissions != permissions:
            click.echo(f"{_file} has {permissions}, should be {expected_permissions}")

if __name__ == "__main__":
    main()