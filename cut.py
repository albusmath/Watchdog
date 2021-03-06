# -*- coding: utf-8 -*-
'''
	cut ``dong dong dong'' out from wav file
'''
import sys
import math
import wave
import numpy as np
import pylab as pl

framerate = 8000

def plot_graph(array, scale=1.0):
	size = len(array)
	time = np.arange(0, size)*scale

	pl.subplot(111) 
	pl.plot(time, array)
#	pl.xlabel("time (seconds)")
	pl.show()

def _get_upperbound(array):
	array = abs(array)
	array = sorted(array, reverse=True)
	return array[len(array)/100]

# get_wave(r"./dong2.wav")
def get_wave(fstr):
	global framerate
#打开wav文件
#open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据
	f = wave.open(fstr, "rb")
# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
	params = f.getparams()
	nchannels, sampwidth, framerate, nframes = params[:4]
# above info must be (1, 2, 8000, ...)
	print "get_wave >>> wave format :", params
# 读取波形数据
	str_data = f.readframes(nframes)
	f.close()
#将波形数据转换为数组
	wave_data = np.fromstring(str_data, dtype=np.short)
#	plot_graph(wave_data)
	return wave_data

def get_cut(wave_data):
	maxdelta = 0.01
	upbound = _get_upperbound(wave_data)
	shout = filter(lambda i: abs(wave_data[i]) > upbound, range(0, len(wave_data))) 
	shout = map(lambda i: float(i) / framerate, shout)

	begin = shout[0]
	for i in range(1, len(shout)):
		if abs(shout[i] - shout[i-1]) > maxdelta:
			break
		else:
			end = shout[i]
	print "get_wave >>> begin, end = ", begin, end
	end += 0.01

	cutout = filter(lambda i: float(i)/framerate >= begin and float(i)/framerate <= end, range(0, len(wave_data)))
	cutout = map(lambda i: wave_data[i], cutout)

	return cutout

def main():
	global framerate
	wave_data = get_wave(r"./dong.wav")
	plot_graph(wave_data, 1.0/framerate)
	wave_data = get_cut(wave_data)
	plot_graph(wave_data, 1.0/framerate)

if __name__ == "__main__":
	main()
