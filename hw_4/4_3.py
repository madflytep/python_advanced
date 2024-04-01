import multiprocessing
import threading
import time
import codecs
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"{timestamp} - Your message here")

def process_a(input_queue, output_queue):
    def send_message():
        while True:
            message = input_queue.get()  # Blocking call, waits for a message
            if message is None:  # Termination signal
                break
            processed_message = message.lower()
            time.sleep(5)  # Wait for 5 seconds before sending
            output_queue.put(processed_message)
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Process A sent: {processed_message}")
    
    thread = threading.Thread(target=send_message)
    thread.start()
    thread.join()

def process_b(input_queue, main_process_queue):
    while True:
        message = input_queue.get()  # Blocking call, waits for a message
        if message is None:  # Termination signal
            break
        encoded_message = codecs.encode(message, 'rot_13')
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Process B encoded and sent: {encoded_message}")
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
    messages = ["Hello, World!", "Goodnight, Moon!"]
    for message in messages:
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Main process sending to Process A: {message}")
        queue_main_to_a.put(message)

    # Sending termination signal
    queue_main_to_a.put(None)
    queue_a_to_b.put(None)

    process_a_instance.join()
    process_b_instance.join()

if __name__ == "__main__":
    main()