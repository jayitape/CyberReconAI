"""
CyberRecon AI
Scan ID Generator Module

Version: 1.0.16
"""


from datetime import datetime



def generate_scan_id():

    """
    Generate unique scan identification ID
    """

    timestamp = datetime.now()


    scan_id = (
        "CRAI-"
        +
        timestamp.strftime("%Y%m%d-%H%M%S")
    )


    return scan_id