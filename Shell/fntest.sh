#!/bin/bash

function speak {
    if [ "$1" = "Paris" ]; then
        echo "Language used is French"
    elif [ "$1" = "Hanoi" ]; then
        echo "Language used is Vietnamese, with a little French"
    else
        echo "Language used is English, of one form or another!"
    fi
}

PS3="> "
echo "Let's check the language"
select city in "Paris" "Melbourne" "Toronto" "Seattle" "Hanoi" "exit"
do
    if [ "$city" = "exit" ]; then
        break
    fi
    case $city in
        Paris)
            echo "City is Paris, France"
            speak "Paris"
            ;;
        Melbourne)
            echo "City is Melbourne, Australia"
            speak "Melbourne"
            ;;
        Toronto)
            echo "City is Toronto, Canada"
            speak "Toronto"
            ;;
        Seattle)
            echo "City is Seattle, USA"
            speak "Seattle"
            ;;
        Hanoi)
            echo "City is Hanoi, Vietnam"
            speak "Hanoi"
            ;;
        *)
            echo "Invalid selection"
            ;;
    esac
done
