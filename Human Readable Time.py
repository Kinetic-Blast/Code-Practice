def make_readable(seconds):
    hours = seconds // 3600
    seconds = seconds % 3600
    
    minutes = seconds // 60
    seconds %= 60
    
    return "%02d:%02d:%02d" % (hours, minutes, seconds)
