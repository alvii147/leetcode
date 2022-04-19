# Read from the file words.txt and output the word frequency list to stdout.
# declare associative array to store word frequency
declare -A frequency_hash
# iterate over file lines
while IFS= read -r line || [[ -n "$line" ]]; do
    # iterate over words in line
    for word in ${line[@]}; do
        # if word already exists, increment frequency count
        if [[ -v "frequency_hash[${word}]" ]]; then
            frequency_hash["${word}"]=$((${frequency_hash["${word}"]} + 1));
        # otherwise, set to 1
        else
            frequency_hash["${word}"]=1;
        fi
    done;
done < words.txt;
# sort words by frequency count and print to console
for key in "${!frequency_hash[@]}"; do
    echo "$key ${frequency_hash[$key]}";
done | sort -rn -k 2
