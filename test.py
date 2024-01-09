import threading
import time
import numpy as np
import matplotlib.pyplot as plt

# Global variables for shared data
x_data = np.arange(0, 10, 0.1)
y_data = np.zeros_like(x_data)


# Function to generate data in the background
def generate_data():
    global y_data
    counter = 0
    while True:
        y_data = np.sin(x_data + counter)  # Use counter to create a moving sine wave
        counter += 0.1  # Increment counter for the next iteration
        time.sleep(0.1)  # Simulate some time-consuming data generation

# Create and start the threads with daemon=True

data_thread = threading.Thread(target=generate_data, daemon=True)
data_thread.start()



try:
    while True:
        plt.clf()  # Clear the previous plot
        plt.plot(x_data, y_data, label='Data')
        plt.title('Updating Plot with Threading')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.pause(0.1)  # Pause to allow the plot to update
except KeyboardInterrupt:
    print('Plotting interrupted by user')
    plt.close()
