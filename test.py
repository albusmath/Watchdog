# -*- coding: utf-8 -*-
import os
import math
import thread
from pyaudio import PyAudio, paInt16 
import numpy as np 
from datetime import datetime 
import wave 
import pylab as pl
import cut


WINDOWSIZE	=	0
BUFFSIZE	= 	0

def play():
	print "***------ shuia ------***"

def dot(a, b):
	res = 0.0
	for i in range(0, len(a)/8):
		res += a[i] * b[i].conjugate()
	return res
	
def get_standard():
	global WINDOWSIZE
	std_wave = cut.get_wave(r"./dong1.wav")
	std_wave = cut.get_cut(std_wave)
	WINDOWSIZE = len(std_wave)
	print "WINDOWSIZE", WINDOWSIZE
	return np.fft.fft(std_wave)
	

def main():
	# 开启声音输入
	f_std = get_standard()
	buff = cut.get_wave(r"./dong3.wav")
	max_like = 0.0
	l1 = math.sqrt(abs(dot(f_std, f_std)))
	for i in range(0, len(buff) - WINDOWSIZE):
		f_cur = np.fft.fft(buff[i:i+WINDOWSIZE])
		like = abs(dot(f_cur, f_std))/math.sqrt(abs(dot(f_cur, f_cur)))/l1
		max_like = max(max_like, like)
	print max_like

if __name__ == '__main__':
	main()
