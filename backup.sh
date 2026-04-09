#!/bin/bash
cd /home/hui/agents-factory
git add -A
git commit -m "自动备份 $(date '+%Y-%m-%d %H:%M')" 2>/dev/null
git push 2>/dev/null
