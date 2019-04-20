#!/bin/bash
echo "var blocked_domains = [" > blocked_domains.js
grep "^0\.0\.0\.0" hosts | cut -d ' ' -f2 | sed 's/\([^$]*\)/"*:\/\/*.\1\/*",/' >> blocked_domains.js
echo "];" >> blocked_domains.js