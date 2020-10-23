import numpy as np
import math
import matplotlib.pyplot as plot

# Get x values of the sine wave
time_index = np.arange(0, 65536, 1)
# Amplitude of the sine wave is sine of a variable like time_index
amplitude = np.sin(2 * math.pi * 655 / 65536 * time_index);

#Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(time_index, amplitude)

#Give a title for the sine wave plot
plot.title('Sine wave')

#Give x axis label for the sine wave plot
plot.xlabel('Time_index')

# Give y axis label for the sine wave plot
plot.ylabel('Amplitude=sin(time)')
plot.axhline(y=0, color='k')
plot.show()

with open("output_data.csv","w") as out_file:
    for i in range(len(amplitude)):
        out_string = str(amplitude)
        out_file.write(out_string)

# Comments by Charles Oct/23/2030 : Commit Only
# Comments by Charles Oct/23/2020 : Commit and Push ! 