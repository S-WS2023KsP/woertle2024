@echo off
REM Gerhard Fessler, 2023-09-02, Public Domain
md tmpoff
cd tmpoff
echo irgendwas > off
dir /L/B
del off
cd ..
rd tmpoff
