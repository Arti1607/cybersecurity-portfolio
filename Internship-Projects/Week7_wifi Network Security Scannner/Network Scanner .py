import subprocess

def get_risk_info(security):

    security = security.lower()

    if "open" in security:
        return (
            "CRITICAL",
            [
                "Packet Sniffing",
                "Evil Twin Attack",
                "Man-in-the-Middle Attack"
            ],
            "Avoid sensitive logins and banking transactions."
        )

    elif "wep" in security:
        return (
            "HIGH",
            [
                "Weak Encryption",
                "Easy Password Cracking"
            ],
            "Do not trust this network for important activities."
        )

    elif "wpa" in security and "wpa2" not in security and "wpa3" not in security:
        return (
            "MEDIUM",
            [
                "Older Security Standard"
            ],
            "Use only if WPA2/WPA3 is unavailable."
        )

    elif "wpa2" in security:
        return (
            "LOW",
            [
                "Generally Secure"
            ],
            "Safe for everyday usage."
        )

    elif "wpa3" in security:
        return (
            "VERY LOW",
            [
                "Latest Wireless Security"
            ],
            "Recommended secure network."
        )

    return (
        "UNKNOWN",
        ["Unknown Security Type"],
        "Verify network before connecting."
    )


def scan_wifi():

    print("\n=== Wi-Fi Security Scanner ===\n")

    try:

        output = subprocess.check_output(
            ["netsh", "wlan", "show", "networks"],
            shell=True
        ).decode("utf-8", errors="ignore")

        networks = []
        security_types = []

        lines = output.split("\n")

        for line in lines:

            line = line.strip()

            if line.startswith("SSID") and "BSSID" not in line:
                ssid = line.split(":", 1)[1].strip()
                networks.append(ssid)

            if line.startswith("Authentication"):
                auth = line.split(":", 1)[1].strip()
                security_types.append(auth)

        print("----- Available Wi-Fi Networks -----\n")

        total = len(networks)
        open_count = 0
        secure_count = 0

        for i in range(total):

            security = (
                security_types[i]
                if i < len(security_types)
                else "Unknown"
            )

            risk, threats, recommendation = get_risk_info(security)

            print(f"Network Name : {networks[i]}")
            print(f"Security Type: {security}")
            print(f"Risk Level   : {risk}")

            print("Possible Threats:")

            for threat in threats:
                print(f"  - {threat}")

            print(f"Recommendation: {recommendation}")

            if risk == "CRITICAL":
                open_count += 1
            else:
                secure_count += 1

            print("-" * 50)

        print("\n===== Security Summary =====")
        print(f"Total Networks Found : {total}")
        print(f"Open Networks        : {open_count}")
        print(f"Secured Networks     : {secure_count}")

    except Exception as e:
        print("Error scanning Wi-Fi:", e)


scan_wifi()