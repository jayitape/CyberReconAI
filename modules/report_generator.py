"""
CyberRecon AI
Professional HTML Report Generator
Version: 1.0.16
"""

import os
from datetime import datetime


def clean_ssl_info(ssl_info):
    """
    Convert SSL raw data into professional format
    """

    cleaned = {}

    subject = ssl_info.get("subject", "")
    issuer = ssl_info.get("issuer", "")


    # Certificate Name
    if "*.google.com" in str(subject):
        certificate = "*.google.com"
    else:
        certificate = str(subject)


    cleaned["Certificate"] = certificate


    # Issuer
    if "Google Trust Services" in str(issuer):
        cleaned["Issuer"] = "Google Trust Services"
    else:
        cleaned["Issuer"] = str(issuer)


    # Country
    if "US" in str(issuer):
        cleaned["Country"] = "US"
    else:
        cleaned["Country"] = "Unknown"


    cleaned["Valid From"] = ssl_info.get(
        "valid_from",
        "N/A"
    )

    cleaned["Valid Until"] = ssl_info.get(
        "valid_until",
        "N/A"
    )


    cleaned["Remaining"] = (
        str(
            ssl_info.get(
                "days_remaining",
                "N/A"
            )
        )
        + " Days"
    )


    return cleaned




def risk_badge(level):

    level = level.upper()


    if level == "LOW":

        return """
        <span class="low">
        🟢 LOW
        </span>
        """


    elif level == "MEDIUM":

        return """
        <span class="medium">
        🟡 MEDIUM
        </span>
        """


    elif level == "HIGH":

        return """
        <span class="high">
        🔴 HIGH
        </span>
        """


    else:

        return """
        <span class="critical">
        🚨 CRITICAL
        </span>
        """





def generate_report(domain, scan_data):


    os.makedirs(
        "reports",
        exist_ok=True
    )


    filename = (
        domain.replace(
            ".",
            "_"
        )
        +
        "_report.html"
    )


    path = os.path.join(
        "reports",
        filename
    )



    target = scan_data["target_information"]


    score = scan_data["risk_score"]

    risk = scan_data["risk_level"]


    ssl = clean_ssl_info(
        scan_data["ssl_information"]
    )


    html = f"""

<html>

<head>

<title>
CyberRecon AI Report
</title>


<style>


body {{

font-family: Arial;
margin:40px;

background:#f8f9fa;

}}


h1,h2 {{

color:#1f2937;

}}



table {{

width:100%;
border-collapse:collapse;
background:white;

}}



th {{

background:#111827;
color:white;

}}



td,th {{

padding:10px;
border:1px solid #ddd;

}}



.low {{

background:#22c55e;
padding:5px 12px;
border-radius:20px;

color:white;

}}


.medium {{

background:#eab308;
padding:5px 12px;
border-radius:20px;

color:black;

}}



.high {{

background:#ef4444;
padding:5px 12px;
border-radius:20px;

color:white;

}}



.critical {{

background:#7f1d1d;
padding:5px 12px;
border-radius:20px;

color:white;

}}



.footer {{

margin-top:40px;

text-align:center;

color:#555;

font-size:14px;

}}



</style>


</head>



<body>



<h1>
CyberRecon AI
</h1>


<h2>
Website Security Assessment Report
</h2>



<h2>
Executive Summary
</h2>


<p>
<b>Target:</b> {domain}
</p>


<p>
<b>Generated:</b>
{datetime.now()}
</p>


<p>

<b>Security Score:</b>
{score}/100

</p>



<p>

<b>Risk Level:</b>

{risk_badge(risk)}

</p>





<h2>
Target Information
</h2>



<table>

<tr>
<th>
Parameter
</th>

<th>
Value
</th>

</tr>



<tr>

<td>
Domain
</td>

<td>
{target.get("domain")}
</td>

</tr>



<tr>

<td>
URL
</td>

<td>
{target.get("url")}
</td>

</tr>



<tr>

<td>
IP Address
</td>

<td>
{target.get("ip")}
</td>

</tr>



<tr>

<td>
Status
</td>

<td>
{target.get("reachable")}
</td>

</tr>



</table>






<h2>
Security Findings
</h2>



<table>


<tr>

<th>
Severity
</th>

<th>
Issue
</th>

</tr>



"""



    for finding in scan_data["findings"]:

        html += f"""

<tr>

<td>
{finding['risk']}
</td>

<td>
{finding['issue']}
</td>

</tr>

"""


    html += """

</table>





<h2>
SSL/TLS Certificate
</h2>


<table>


<tr>

<th>
Parameter
</th>

<th>
Value
</th>

</tr>


"""



    for k,v in ssl.items():

        html += f"""

<tr>

<td>
{k}
</td>

<td>
{v}
</td>

</tr>


"""



    html += """

</table>





<h2>
Open Ports
</h2>


<table>

<tr>

<th>
Port
</th>

<th>
Service
</th>

<th>
State
</th>


</tr>


"""



    for port in scan_data["ports"]:


        html += f"""

<tr>

<td>
{port['port']}
</td>


<td>
{port['service']}
</td>


<td>
{port['state']}
</td>


</tr>

"""


    html += """

</table>





<h2>
Technology Stack
</h2>



<p>

<b>Server:</b>

"""



    html += ", ".join(
        scan_data["technology_information"]["server"]
    )


    html += """

</p>



<h2>
Recommendations
</h2>


<ul>

<li>
Enable missing security headers.
</li>

<li>
Monitor SSL certificate expiry.
</li>

<li>
Review sensitive paths exposed through robots.txt.
</li>

<li>
Perform regular security assessments.
</li>

</ul>





<div class="footer">


------------------------------------------------


<br>


Generated By:
<br>

<b>
CyberRecon AI v1.0.16
</b>


<br><br>


Authorized Defensive Security Assessment Toolkit


<br><br>


Scan completed successfully.


<br>


------------------------------------------------



</div>




</body>

</html>


"""



    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:


        file.write(
            html
        )



    return path