"""
CyberRecon AI

Scan Duration Timer Module

Version: 1.0.16
"""


from datetime import datetime



def start_timer():

    """
    Start scan timer
    """

    return datetime.now()



def end_timer():

    """
    End scan timer
    """

    return datetime.now()



def calculate_duration(start_time, end_time):

    """
    Calculate scan duration
    """

    duration = end_time - start_time


    return str(duration).split(".")[0]



def get_time():

    """
    Return formatted timestamp
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )