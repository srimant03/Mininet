import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sender-ss1.csv", names=['time', 'sender', 'retx_unacked', 'retx_cum', 'cwnd', 'ssthresh'])

# exclude the "control" flow
s = df.groupby('sender').size()
df_filtered = df[df.groupby("sender")['sender'].transform('size') > 100]

senders = df_filtered.sender.unique()

time_min = df_filtered.time.min()
cwnd_max = 1.1*df_filtered[df_filtered.time - time_min >=2].cwnd.max()
dfs = [df_filtered[df_filtered.sender==senders[i]] for i in range(3)]

print(df_filtered.head())

#plot cwnd vs time for each flow
time_values = []
cwnd_values = []
for i in range(len(senders)):
    time_values.append(df_filtered[df_filtered.sender==senders[i]]['time'].values)
    cwnd_values.append(df_filtered[df_filtered.sender==senders[i]]['cwnd'].values)

n=len(cwnd_values)
for i in range(n):
    plt.plot(time_values[i]-time_min, cwnd_values[i], label="cwnd")
    plt.ylim([0,cwnd_max])
    plt.xlabel("Time (s)")
    plt.ylabel("Congestion Window Size")
    plt.title("Congestion Window vs. Time")
    plt.grid(True)
    plt.show()
