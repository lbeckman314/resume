#!/bin/bash
pkgs=(
    easylist
    enumitem
    eso-pic
    geometry
    hyperref
    tikzpagenodes
    titling
    xcolor
)

echo "Installing:"
i=1
for pkg in ${pkgs[*]}
do
    echo "  $i) $pkg"
    ((i++))
done
tlmgr install ${pkgs[*]}
