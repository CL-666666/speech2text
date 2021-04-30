#!/bin/bash
ffmpeg -i $1 -f segment -segment_time 60 -c copy out/audio%02d.wav
for file in out/*
do
    if [ -f "$file" ]
    then
        ffmpeg -y -i ${file%%.*}.wav -acodec pcm_s16le -f s16le -ac 1 -ar 16000 ${file%%.*}.pcm
        
    fi
done
rm -rf out/*.wav