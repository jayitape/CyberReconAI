"""
CyberRecon AI

Port Scanner Module

Authorized Defensive Security Assessment Toolkit

Purpose:
- Discover open TCP ports
- Identify common services
- Perform basic banner grabbing
"""


import socket

from typing import Dict, List


from modules.logger import setup_logger



logger = setup_logger()



COMMON_PORTS = {

    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy"

}




def grab_banner(
        target: str,
        port: int
) -> str:
    """
    Attempt to grab service banner.

    Args:
        target: Target hostname/IP
        port: Open port number

    Returns:
        Service banner information
    """

    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(2)


        sock.connect(
            (target, port)
        )


        sock.send(
            b"HEAD / HTTP/1.0\r\n\r\n"
        )


        banner = sock.recv(
            1024
        ).decode(
            errors="ignore"
        )


        sock.close()


        return banner.strip()



    except Exception:

        return "Unknown"





def scan_port(
        target: str,
        port: int
) -> bool:
    """
    Check whether TCP port is open.

    Args:
        target: Target hostname/IP
        port: Port number

    Returns:
        True if open else False
    """

    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )


        socket.setdefaulttimeout(
            1
        )


        result = sock.connect_ex(
            (target, port)
        )


        sock.close()



        if result == 0:

            return True


        return False



    except Exception as error:


        logger.error(
            "Port scan error %s:%s - %s",
            target,
            port,
            error
        )


        return False





def scan_ports(
        target: str
) -> List[Dict[str, object]]:
    """
    Scan common TCP ports.

    Args:
        target: Target domain

    Returns:
        List containing open port details
    """


    logger.info(
        "Starting port scan on %s",
        target
    )



    results = []



    for port, service in COMMON_PORTS.items():


        if scan_port(
            target,
            port
        ):


            banner = grab_banner(
                target,
                port
            )



            results.append(

                {
                    "port": port,
                    "service": service,
                    "state": "OPEN",
                    "banner": banner
                }

            )


            logger.info(
                "Open port detected: %s/%s",
                port,
                service
            )



    logger.info(
        "Port scanning completed"
    )


    return results