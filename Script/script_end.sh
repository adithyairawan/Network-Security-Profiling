!# bin/sh
#sudo airmon-ng start wlan0
#dumpcap -c 20000 -f icmp -w /media/adit/TOSHIBA/data/edit/possatt.pcapn
tshark -2 -R "wlan_radio.signal_dbm<0" -Y "wlan.addr == d0:37:45:73:ed:7c" -r /media/adit/TOSHIBA/data/edit/possatt.pcapng -T fields -e wlan_radio.signal_dbm -E header=y -E separator=, -E quote=d -E occurrence=f > /media/adit/TOSHIBA/data/edit/Attack_data/csv/attack_automate_down.csv
tshark -2 -R "wlan_radio.signal_dbm<0" -Y "wlan.addr == b8:27:eb:0f:dc:e0" -r /media/adit/TOSHIBA/data/edit/possatt.pcapng -T fields -e wlan_radio.signal_dbm -E header=y -E separator=, -E quote=d -E occurrence=f > /media/adit/TOSHIBA/data/edit/Attack_data/csv/attack_automate_up.csv
#sudo airmon-ng stop wlan0mon
# python csv_process.py
# python experiment.py
# python ipfilter.py

