import random
import csv
import matplotlib.pyplot as plt

times = []
temps = []
humidities = []

filename = "data_log.csv"
try:    
   with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Time (s)", "Temperature (C)", "Humidity (%)"])

            for i in range(10):
                t = i
                temp = random.uniform(20, 30)
                humidity = random.uniform(40, 60)

                writer.writerow([t, temp, humidity])
                times.append(t)
                temps.append(temp)
                humidities.append(humidity)

   print("Data saved finally.")
 
except Exception as e:
      print(f"An error occurred: {e}")
plt.plot(times,temps,label="Temperature")
plt.plot(times, humidities, label="Humidity")
plt.title("Temperature and Humidity over Time")
plt.legend()
plt.show()
    
