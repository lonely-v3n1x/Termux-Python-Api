#!/data/data/com.termux/files/usr/bin/sh
set -e -u

mkdir $(pwd)/bin
gcc ./api-scripts/termux-api.c -std=c11 -Wall -Wextra -pedantic -Werror -o ./bin/termapi
install ./api-scripts/termux-callback ./bin

termux-elf-cleaner ./bin/termapi

