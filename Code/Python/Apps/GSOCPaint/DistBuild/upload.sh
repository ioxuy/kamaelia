#!/bin/sh



version=`grep version setup.py.src|sed -e 's/^.*= "//; s/",.*//'`
echo "Uploading GSOC Paint application distribution $version"

scp ../dist/* michaels@132.185.142.2:/srv/www/sites/www.kamaelia.org/docs/release/