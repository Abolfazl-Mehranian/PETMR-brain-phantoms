
function bar = os_bar()
if(strcmp(computer(), 'GLNXA64')) % If linux, call wine64.
    bar = '/';
else
    bar = '\';
end