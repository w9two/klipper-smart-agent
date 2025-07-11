from config_parser import analyze_config
from log_watcher import watch_logs
from ai_agent import send_prompt
import argparse

def main(config_path, log_path):
    print("[*] Analyzing configuration...")
    config_summary = analyze_config(config_path)

    print("[*] Monitoring logs...")
    recent_logs = watch_logs(log_path)

    print("[*] Sending to AI agent...")
    response = send_prompt(config_summary, recent_logs)

    print("\n===== AI Response =====")
    print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="/home/pi/printer_data/config/printer.cfg", help="Path to printer.cfg")
    parser.add_argument("--log", default="/home/pi/printer_data/logs/klippy.log", help="Path to klippy.log")
    args = parser.parse_args()

    main(args.config, args.log)
