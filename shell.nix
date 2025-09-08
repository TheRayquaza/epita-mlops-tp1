{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixos-23.11.tar.gz") {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311
    pkgs.python312Packages.virtualenv
  ];
 
  shellHook = ''
    VENV_DIR=".venv"

    if [ ! -d "$VENV_DIR" ]; then
      python -m venv "$VENV_DIR"
      source "$VENV_DIR/bin/activate"
    else
      echo "Using existing virtualenv in $VENV_DIR"
      source "$VENV_DIR/bin/activate"
    fi
  '';
}
