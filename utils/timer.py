import time
from datetime import datetime

def format_time(seconds):
    """Format seconds into MM:SS"""
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def get_time_remaining(start_time, limit_seconds):
    """Calculate remaining time based on start time and limit"""
    elapsed = time.time() - start_time
    remaining = limit_seconds - elapsed
    return max(0, remaining)
