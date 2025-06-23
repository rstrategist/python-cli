import subprocess
import shlex
import json
import click
from pprint import pprint


# create a function that runs suprocess and returns the output
def run_command(command):
    """Runs a shell command and returns the output."""
    cmd = shlex.split(command)
    output = subprocess.check_output(cmd)
    return output


def run_lsblk(device, nice=False):
    """
    Runs lsblk command and produces JSON output:

    lsblk -J -o NAME,SIZE,TYPE,MOUNTPOINT
    {
    "blockdevices": [
        {"name": "vda", "size": "59.6G", "type": "disk", "mountpoint": null,
            "children": [
                {"name": "vda1", "size": "59.6G", "type": "part", "mountpoint": "/etc/hosts"}
            ]
        }
    ]
    }
    """
    command = "lsblk -J -o NAME,SIZE,TYPE,MOUNTPOINT"
    # run the command
    try:
        output = run_command(command)
        devices = json.loads(output)["blockdevices"]

        for parent in devices:
            if parent["name"] == device:
                if nice:
                    return pprint(parent)
            for child in parent.get("children", []):
                if child["name"] == device:
                    if nice:
                        return pprint(child)
                    return child
        # if device not found
        click.echo(click.style("Device not found:", fg="red"))
        return f"{str(device)}"
        # if verbose:
        #    raise

    # handle exceptions
    except (subprocess.CalledProcessError, json.JSONDecodeError) as err:
        click.echo(click.style("Error running lsblk:", fg="red"))
        return f"{str(err)}"
