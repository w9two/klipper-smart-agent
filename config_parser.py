def analyze_config(config_path):
    try:
        with open(config_path, 'r') as f:
            lines = f.readlines()
        # Basic cleaning
        filtered = [line for line in lines if line.strip() and not line.strip().startswith("#")]
        return "\n".join(filtered[:300])  # Limit to 300 lines
    except Exception as e:
        return f"Error reading config: {e}"
