echo "Launching tests"

tests=("1 + 2"\
        "2 ^ 2 * 2 / 2"\
        "1 + 3 * (2 - 1) ^ 2"\
        "-1 + 2"\
        "199 + 1")
resuts=("3"\
        "4.0"\
        "4"\
        "1"\
        "200")

for ((i=0;i<${#tests[@]};++i)); do
    res=`python3 main.py "${tests[i]}"`
    if [ "$res" != "${resuts[i]}" ]
    then
        printf "Expected:\t%s = %s\n" "${tests[i]}" "${resuts[i]}"
        printf "Actual:\t\t%s = %s\n" "${tests[i]}" "$res"
    fi;
done

echo "Done"
