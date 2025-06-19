import schedule
import time

def display():
    print("Namaskar🙏...")

def main():
    schedule.every().days.at("9:00 AM").do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()