from datetime import datetime, timedelta

def watch_logs(log_path, minutes=5):
    try:
        with open(log_path, 'r') as f:
            lines = f.readlines()
        recent_lines = []
        now = datetime.now()
        for line in reversed(lines):
            if "]" in line and ":" in line:
                try:
                    timestamp_str = line.split("]")[0].strip(" [")
                    timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")
                    timestamp = timestamp.replace(year=now.year)
                    if now - timestamp < timedelta(minutes=minutes):
                        recent_lines.append(line)
                    else:
                        break
                except:
                    continue
        return "".join(reversed(recent_lines))
    except Exception as e:
        return f"Error reading log: {e}"
