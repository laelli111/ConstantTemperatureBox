import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import serial
import plotly.tools as tls


# Username, apikey and streamtokens for Plot.ly web service
# One streamtoken for each stream, 6 per box 
username = '****'
api_key = '****'
stream_tokens = ['****', '****', '****', '****', '****', '****', '****','****','****','****','****','****']
py.sign_in(username, api_key)

# Structures for each data value. See plot.ly for examples

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


measured_temp2 = Scatter(
    x=[],
    y=[],
    name = "Measured temperature 2",
    xaxis='x3',
    yaxis='y3',
    stream=dict(
        token=stream_tokens[6],
        maxpoints=200
    )
)

sample_est2 = Scatter(
    x=[],
    y=[],
    xaxis='x3',
    yaxis='y3',
    name = "Sample temperature estimate 2",
    stream=dict(
        token=stream_tokens[7],
        maxpoints=200
    )
)

target2 = Scatter(
    x=[],
    y=[],
    name = "Target temperature 2",
    xaxis='x3',
    yaxis='y3',
    stream=dict(
        token=stream_tokens[8],
        maxpoints=200
    )
)

heater_est2 = Scatter(
    x=[],
    y=[],
    name = "Heater temperature estimate 2",
    xaxis='x4',
    yaxis='y4',
    stream=dict(
        token=stream_tokens[9],
        maxpoints=200
    )
)

air_est2 = Scatter(
    x=[],
    y=[],
    name = "Air temperature estimate 2",
    xaxis='x3',
    yaxis='y3',
    stream=dict(
        token=stream_tokens[10],
        maxpoints=200
    )
)

heaterPWM2 = Scatter(
    x=[],
    y=[],
    name = "Heater PWM 2",
    xaxis='x4',
    yaxis='y4',
    stream=dict(
        token=stream_tokens[11],
        maxpoints=200
    )
)


# Set title

layout = Layout(
    title='Raspberry Pi Streaming Temperature Boxes'
)

#Plotting one figure
#fig = Figure(data=[measured_temp, sample_est], layout=layout)


# Plotting subplots
data = [target, measured_temp, heater_est, air_est, sample_est, heaterPWM, target2, measured_temp2, heater_est2, air_est2, sample_est2, heaterPWM2]
fig = tls.get_subplots(rows=2, columns=2)
fig['data'] += data
fig['layout'].update(title='Raspberry Pi Streaming Temperature Boxes')
fig['layout'].update(showlegend=True)

print py.plot(fig, filename='Raspberry Pi Streaming Temperature Boxes')

# Open a stream for each data structure

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
stream7 = py.Stream(stream_tokens[6])
stream7.open()
stream8 = py.Stream(stream_tokens[7])
stream8.open()
stream9 = py.Stream(stream_tokens[8])
stream9.open()
stream10 = py.Stream(stream_tokens[9])
stream10.open()
stream11 = py.Stream(stream_tokens[10])
stream11.open()
stream12 = py.Stream(stream_tokens[11])
stream12.open()



# Open serial connection: check ports! 
# Ports are usually 0 and 1 after reboot

ser1 = serial.Serial('/dev/ttyUSB0', 9600)
ser2 = serial.Serial('/dev/ttyUSB1', 9600)

# The main serial data reading loop


# Skip a line including column headers (csv format)
ser1.readline()
ser2.readline()

while True:
	
	# Read line from serial
	data_in1 = ser1.readline()
	data_in2 = ser2.readline()
	
	# Parse CSV
	values = data_in1.split(';')
	time_ms = values[0]
	target = values[1]
	measured = values[2]
	heaterPWM = values[3]
	heater_est = values[4]
	air_est = values[5]
	sample_est = values[6]
	# Parse CSV
	values2 = data_in2.split(';')
	time_ms2 = values2[0]
	target2 = values2[1]
	measured2 = values2[2]
	heaterPWM2 = values2[3]
	heater_est2 = values2[4]
	air_est2 = values2[5]
	sample_est2 = values2[6]        
	       	
	# Write values to streams
	stream1.write({'x': time_ms, 'y': measured})
	stream2.write({'x': time_ms, 'y': sample_est})
	stream3.write({'x': time_ms, 'y': target})
	stream4.write({'x': time_ms, 'y': heater_est})
	stream5.write({'x': time_ms, 'y': air_est})
	stream6.write({'x': time_ms, 'y': heaterPWM})

	stream7.write({'x': time_ms2, 'y': measured2})
	stream8.write({'x': time_ms2, 'y': sample_est2})
	stream9.write({'x': time_ms2, 'y': target2})
	stream10.write({'x': time_ms2, 'y': heater_est2})
	stream11.write({'x': time_ms2, 'y': air_est2})
	stream12.write({'x': time_ms2, 'y': heaterPWM2})
	
        # delay between stream posts
        time.sleep(1)
