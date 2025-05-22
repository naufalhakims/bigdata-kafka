from confluent_kafka import Producer
import json
import time
import random

conf = {'bootstrap.servers': 'kafka:9092'}  # kafka adalah nama service di docker-compose
producer = Producer(conf)

gudang_ids = ['G1', 'G2', 'G3']

def delivery_report(err, msg):
    if err is not None:
        print(f"Gagal mengirim pesan: {err}")
    else:
        print(f"Data terkirim: {msg.value().decode('utf-8')}")
        #print(f"Pesan berhasil dikirim ke topik {msg.topic()} partisi [{msg.partition()}]")

try:
    while True:
        for gudang_id in gudang_ids:
            suhu = random.randint(75, 90)
            data = {"gudang_id": gudang_id, "suhu": suhu}
            producer.produce("sensor-suhu-gudang", json.dumps(data).encode('utf-8'), callback=delivery_report)
            producer.poll(0)
        time.sleep(1)
except KeyboardInterrupt:
    print("Pengiriman data suhu dihentikan.")
finally:
    producer.flush()
