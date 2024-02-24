from thefuck.specific.nix import nix_available
import subprocess

enabled_by_default = nix_available

# Set the priority just ahead of `fix_file` rule, which can generate low quality matches due
# to the sheer amount of paths in the nix store.
priority = 999


def match(command):
    return (
        "NIXPKGS_ALLOW_UNFREE=1" in command.output
    )


def get_new_command(command):
    commands = [
        'NIXPKGS_ALLOW_UNFREE=1 {}'.format(command.script)
    ]
    return commands
