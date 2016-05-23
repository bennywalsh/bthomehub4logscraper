#!/bin/bash

logFile=$1

while read line
do
        for word in $line
        do
                # if word is ip address change to hostname
                if [[ $word =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]
                then
                        # check if ip address is correct
                        OIFS=$IFS
                        IFS="."
                        ip=($word)
                        IFS=$OIFS
                        if [[ ${ip[0]} -le 255 && ${ip[1]} -le 255 && ${ip[2]} -le 255 && ${ip[3]} -le 255 ]]
                        then
                                echo -n `host $word | cut -d' ' -f 5`
                                echo -n " "
                        else
                                echo -n "$word"
                                echo -n " "
                        fi
                # else print word
                else
                        echo -n $word
                        echo -n " "
                fi
        done
        # new line
        echo
done < "$logFile"
