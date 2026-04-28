#!/bin/sh
export PATH="$HOME/.local/bin:/usr/bin:/bin"
voice-mode --help 2>&1 | head -100
