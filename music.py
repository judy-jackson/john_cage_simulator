# audio.py
#
# Judy Jackson
# 12/19/14

import audio
import math

class Music:
    
    def __init__(self, halftones = 0, duration = 0, amp = 1, samplerate =44100):
        if (isinstance(halftones, str) == True):
            self.samples = audio.read_file(halftones)
            self.maxvol = max(self.samples)
            self.length = len(self.samples)
        else:    
            frequency = 440*(2**((halftones+3)/12))
            sample_number = int(duration * samplerate)
            self.samples = []
            for i in range (sample_number):
                y = amp * (math.sin((frequency * (math.pi) * i)/samplerate))
                self.samples.append(y)
    
    def play(self):
        audio.play(self.samples)
        
    def concat(self, s2):
        a = self.samples
        b = s2.samples
        new = a.extend(b)
        self = new
        
    def plus(self, s2):       
        small = min(len(self.samples), len(s2.samples))
        for i in range(small):
            self.samples.append(self.samples[i] + s2.samples[i])
        return self
        
