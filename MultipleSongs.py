__author__ = 'brothertonjd'
import echonest.remix.audio as audio
import FindBranches as fb
import os
import pickle
import hashlib
import BeatDistance
from pyechonest import config
config.ECHO_NEST_API_KEY="OLUEAY4CYBN5MTBLW"
filename = "C:\\Users\\brothertonjd\\PycharmProjects\\testplayer\\poop.mp3"
filename2 = "C:\\Users\\brothertonjd\\PycharmProjects\\testplayer\\poop2.mp3"
audio_file = audio.LocalAudioFile(filename)
audio_file2 = audio.LocalAudioFile(filename2)
beats = audio_file.analysis.beats
beats2 = audio_file2.analysis.beats
branches = {}
song1 = {}
test = {}
song2 = {}

if ".remix-db/audio" in audio_file.filename:
    filename = os.path.splitext(os.path.split(audio_file.filename)[1])[0]
else:
    filename = hashlib.md5(file(audio_file.filename, 'rb').read()).hexdigest()

if ".remix-db/audio" in audio_file.filename:
    filename2 = os.path.splitext(os.path.split(audio_file2.filename)[1])[0]
else:
    filename2 = hashlib.md5(file(audio_file2.filename, 'rb').read()).hexdigest()

for i in range (len(beats)):
    beat1 = beats[i]
    for j in range (len(beats2)):
        beat2 = beats2[j]
        if beat1.local_context()[0] == beat2.local_context()[0]:
                dist = BeatDistance.get_beat_distance(beat1, beat2)
                if dist <= 80:
                    if song1.has_key(i):
                        song1[i].append((j, dist))
                    else:
                        song1[i] = [(j, dist)]

                    if song2.has_key(j):
                        song2[j].append((i, dist))
                    else:
                        song2[j] = [(i, dist)]

print song1
print song2

"""
for i in range (len(beats2)):
    beat1 = beats2[i]
    for j in range (len(beats)):
        beat2 = beats[j]
        if beat1.local_context()[0] == beat2.local_context()[0]:
                dist = BeatDistance.get_beat_distance(beat2, beat1)
                if dist <= 80:
                    if song2.has_key(i):
                        song2[i].append((j, dist))
                    else:
                        song2[j] = [(i, dist)]
                    if song2.has_key(j):
                        song2[j].append((i, dist))
                    else:
                        song2[i] = [(j, dist)]



print song2
"""
"""for i in range(len(beats)):
        beat1 = beats[i]
        for j in range(i+1,len(beats)):
            beat2 = beats[j]
            if beat1.local_context()[0] == beat2.local_context()[0]:
                dist = BeatDistance.get_beat_distance(beat1, beat2)
                if dist <= 80:
                    if branches.has_key(i):
                        branches[i].append((j, dist))
                    else:
                        branches[i] = [(j, dist)]
                    if branches.has_key(j):
                        branches[j].append((i, dist))
                    else:
                        branches[j] = [(i, dist)]
print branches

for i in range(len(beats2)):
        beat1 = beats2[i]
        for j in range(i+1,len(beats2)):
            beat2 = beats2[j]
            if beat1.local_context()[0] == beat2.local_context()[0]:
                dist = BeatDistance.get_beat_distance(beat1, beat2)
                if dist <= 80:
                    if test.has_key(i):
                        test[i].append((j, dist))
                    else:
                        test[i] = [(j, dist)]
                    if test.has_key(j):
                        test[j].append((i, dist))
                    else:
                        test[j] = [(i, dist)]
print test"""
"""for i in range (len(beats)- 1):
    beat3 = beats[i]

    beat4 = beats[i + 1]
    if beat3.local_context()[0] == beat4.local_context()[0]:
        dist = BeatDistance.get_beat_distance(beat3, beat4)
        if dist <= 80:
            if test.has_key(i):
                 test[i].append((i, dist))
            else:
                test[i] = [(i, dist)]

print test"""

"""for i in range (len(beats2)):
    beat2 = beats[i]
    for j in range (len(beats)):
        beat1 = beats2[j]
        if beat1.local_context()[0] == beat2.local_context()[0]:
                dist = BeatDistance.get_beat_distance(beat1, beat2)
                if dist <= 80:
                    if branches.has_key(i):
                        branches[i].append((j, dist))
                    else:
                        branches[i] = [(j, dist)]
                    if branches.has_key(j):
                        branches[j].append((i, dist))
                    else:
                        branches[j] = [(i, dist)]
print branches
"""


if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/Branches"):
    os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "/Branches")
with open(os.path.dirname(os.path.realpath(__file__)) + "/Branches/" + filename + "_" + filename2 + ".pkl", 'w') as outfile:
    pickle.dump(song1, outfile)

if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/Branches"):
    os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "/Branches")
with open(os.path.dirname(os.path.realpath(__file__)) + "/Branches/" + filename2 + "_" + filename + ".pkl", 'w') as outfile:
    pickle.dump(song2, outfile)