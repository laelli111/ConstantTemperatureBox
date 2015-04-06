import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import serial
import plotly.tools as tls

username = 'laelli'
api_key = 'au71fi2g3w'
stream_tokens = ['3g5te13mdn', '7gy2tn8fz9', 'pq5xkrdgww', 'pjcg8ssfhk', 'fz3q1texzq', '2w6u4lwmpj', 'ionn3gjips']

py.sign_in(username, api_key)

measured_temp = Scatter(
    x=[],
    y=[],
    name = "Measured temperature",
    xaxis='x1',
    yaxis='y1',
    stream=dict(
        token=stream_tokens[0],
        maxpoints=200
    )
)

sample_est = Scatter(
    x=[],
    y=[],
    xaxis='x1',
    yaxis='y1',
    name = "Sample temperature estimate",
    stream=dict(
        token=stream_tokens[1],
        maxpoints=200
    )
)

target = Scatter(
    x=[],
    y=[],
    name = "Target temperature",
    xaxis='x1',
    yaxis='y1',
    stream=dict(
        token=stream_tokens[2],
        maxpoints=200
    )
)

heater_est = Scatter(
    x=[],
    y=[],
    name = "Heater temperature estimate",
    xaxis='x2',
    yaxis='y2',
    stream=dict(
        token=stream_tokens[3],
        maxpoints=200
    )
)

air_est = Scatter(
    x=[],
    y=[],
    name = "Air temperature estimate",
    xaxis='x1',
    yaxis='y1',
    stream=dict(
        token=stream_tokens[4],
        maxpoints=200
    )
)

heaterPWM = Scatter(
    x=[],
    y=[],
    name = "Heater PWM",
    xaxis='x2',
    yaxis='y2',
    stream=dict(
        token=stream_tokens[5],
        maxpoints=200
    )
)

layout = Layout(
    title='Raspberry Pi Streaming Temperature Boxes'
)

#fig = Figure(data=[measured_temp, sample_est], layout=layout)

data = [target, measured_temp, heater_est, air_est, sample_est, heaterPWM]
fig = tls.get_subplots(rows=1, columns=2)
fig['data'] += data
fig['layout'].update(title='Raspberry Pi Streaming Temperature Boxes')
fig['layout'].update(showlegend=True)

print py.plot(fig, filename='Raspberry Pi Streaming Box 1 Values')

stream1 = py.Stream(stream_tokens[0])
stream1.open()
stream2 = py.Stream(stream_tokens[1])
stream2.open()
stream3 = py.Stream(stream_tokens[2])
stream3.open()
stream4 = py.Stream(stream_tokens[3])
stream4.open()
stream5 = py.Stream(stream_tokens[4])
stream5.open()
stream6 = py.Stream(stream_tokens[5])
stream6.open()



#open serial connection: check ports!
ser1 = serial.Serial('/dev/ttyUSB0', 9600)
#ser2 = serial.Serial('/dev/ttyUSB1', 57600)

#the main serial data reading loop
temp = ser1.readline()
while True:
	data_in1 = ser1.readline()
	#data_in2 = ser2.readline()
	values = data_in1.split(';')
	time_ms = values[0]
	target = values[1]
	measured = values[2]
	heaterPWM = values[3]
	heater_est = values[4]
	air_est = values[5]
	sample_est = values[6]        
	       	

	stream1.write({'x': time_ms, 'y': measured})
	stream2.write({'x': time_ms, 'y': sample_est})
	stream3.write({'x': time_ms, 'y': target})
	stream4.write({'x': time_ms, 'y': heater_est})
	stream5.write({'x': time_ms, 'y': air_est})
	stream6.write({'x': time_ms, 'y': heaterPWM})
	
        # delay between stream posts
        time.sleep(1)
