import click
from blkpy.util import run_lsblk
from blkpy.file_utils import list_files


# create the click commands
@click.group()
def cli():
    """blkpy: A simple CLI tool for inspecting block devices and listing files."""
    pass


@cli.command()
@click.option("--verbose", "-v", is_flag=True)
@click.argument("device")
def inspect(device, verbose):
    """
    Inspect a block device.

    DEVICE: The name of the block device to inspect.

    Examples:
        blkpy inspect vda
        blkpy inspect --verbose vda
    """
    print(f"Device: {device}")
    print(f"Verbose: {verbose}")
    print(f"{run_lsblk(device)}")


@cli.command()
@click.option("--recursive", "-r", is_flag=True, help="List files recursively.")
@click.option("--extension", "-e", default=None, help="Filter files by extension.")
@click.argument("directory")
def listfiles(directory, recursive, extension):
    """
    List files in a directory.

    DIRECTORY: The path of the directory to list files from.

    Examples:
        blkpy listfiles /path/to/directory
        blkpy listfiles --recursive /path/to/directory
        blkpy listfiles --extension .txt /path/to/directory
        blkpy listfiles --recursive --extension .txt /path/to/directory
    """
    files = list_files(directory, recursive, extension)
    for file in files:
        print(file)


if __name__ == "__main__":
    cli()
