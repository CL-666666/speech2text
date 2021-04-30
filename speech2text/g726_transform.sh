#!/bin/bash
ffmpeg -f g726 -ar 8000 -code_size 2 -i $1 -acodec pcm_s16le -ar 8000 -ac 1 out.wav
ffmpeg -i out.wav -f segment -segment_time 60 -c copy out/audio%02d.wav
for file in out/*
do
    if [ -f "$file" ]
    thens
        ffmpeg -y -i ${file%%.*}.wav -acodec pcm_s16le -f s16le -ac 1 -ar 16000 ${file%%.*}.pcm
        
    fi
done
rm -rf out/*.wav