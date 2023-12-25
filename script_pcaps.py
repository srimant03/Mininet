from scapy.all import *
import matplotlib.pyplot as plt

def get_congestion_window_size(pcap_file):
    packets = rdpcap(pcap_file)
    seq_no = {}
    cwnd= []
    for packet in packets:
        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            key = (packet[IP].src, src_port, packet[IP].dst, dst_port)

            if key not in seq_numbers:
                seq_no[key] = []

            # Track sequence numbers
            seq_no[key].append(packet[TCP].seq)

            # Calculate congestion window size
            cwnd = max(seq_no[key]) - min(seq_no[key])
            cwnd.append(cwnd)

    return cwnd

def plot_cwnd_vs_time(time_values, cwnd_values):
    plt.plot(time_values, cwnd_values)
    plt.title('Congestion Window vs. Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Congestion Window Size')
    plt.grid(True)
    plt.show()

pcap_file = 'test.pcap'
cwnd_sizes = get_congestion_window_size(pcap_file)

time_values = [i * 0.001 for i in range(len(cwnd_sizes))]  
plot_cwnd_vs_time(time_values, cwnd_sizes)
