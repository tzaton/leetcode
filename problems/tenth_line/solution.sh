# Read from the file file.txt and output the tenth line to stdout.
if [ "$(wc -l file.txt | cut -f1 -d ' ')" -lt 10 ]; then
    echo
else
    head -n 10 file.txt | tail -n 1 
fi