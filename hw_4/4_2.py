import multiprocessing
import threading
import time
import codecs
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='hw_4/artifacts/4_3_logs.txt',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def process_a(input_queue, output_queue):
    def send_message():
        while True:
            message = input_queue.get()  
            if message is None:  
                break
            processed_message = message.lower()
            time.sleep(5) 
            output_queue.put(processed_message)
            logging.info(f"Process A sent: {processed_message}")
    
    thread = threading.Thread(target=send_message)
    thread.start()
    thread.join()

def process_b(input_queue, main_process_queue):
    while True:
        message = input_queue.get() 
        if message is None: 
            break
        encoded_message = codecs.encode(message, 'rot_13')
        logging.info(f"Process B encoded and sent: {encoded_message}")
        main_process_queue.put(encoded_message)

def main():
    queue_a_to_b = multiprocessing.Queue()
    queue_main_to_a = multiprocessing.Queue()
    queue_b_to_main = multiprocessing.Queue()

    process_a_instance = multiprocessing.Process(target=process_a, args=(queue_main_to_a, queue_a_to_b))
    process_b_instance = multiprocessing.Process(target=process_b, args=(queue_a_to_b, queue_b_to_main))

    process_a_instance.start()
    process_b_instance.start()

    # Example messages
    messages = ["String one", "String two", "String three", "Hello, World!", "Goodnight, Moon!"]
    for message in messages:
        logging.info(f"Main process sending to Process A: {message}")
        queue_main_to_a.put(message)

    queue_main_to_a.put(None)
    queue_a_to_b.put(None)

    process_a_instance.join()
    process_b_instance.join()

if __name__ == "__main__":
    main()
