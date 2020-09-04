#!/bin/bash

Xvfb :99 -screen 0 1920x1080x8 -nolisten tcp &
exec "$@"