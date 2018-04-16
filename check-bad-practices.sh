#!/bin/bash

check_sudo_pip() {
    echo "Scanning $i"
    if grep 'sudo pip' "$i"; then
        >&2 echo "ERROR: pip should never be used as a sudo command."
        >&2 echo "Consider using PEP370 instead via pip's --user parameter."
        >&2 echo "https://www.python.org/dev/peps/pep-0370/"
        exit 1
    fi
}

# Scan files for bad practices
mapfile -t doc_files <<< $(find . -name "*.rst")
for i in "${doc_files[@]}"; do
    check_sudo_pip $i
done
