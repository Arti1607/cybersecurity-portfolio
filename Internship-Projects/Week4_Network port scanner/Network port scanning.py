import socket
import time

def scan_ports(target, start_port, end_port):
    print(f"\nScanning target: {target}")
    print(f"Port range: {start_port} - {end_port}")
    print("Scanning ports... Please wait.\n")

    open_ports = []

    try:
        # Resolve domain to IP (important improvement)
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Hostname could not be resolved.")
        return

    start_time = time.time()

    for port in range(start_port, end_port + 1):
        try:
            # Create socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            result = s.connect_ex((target_ip, port))

            if result == 0:
                print(f"✅ Port {port} is OPEN")
                open_ports.append(port)

            s.close()

        except KeyboardInterrupt:
            print("\n⚠️ Scan interrupted by user.")
            break
        except socket.error:
            print("❌ Could not connect to server.")
            break

    end_time = time.time()

    # Summary (small but powerful improvement)
    print("\n--- Scan Summary ---")
    print(f"Time taken: {round(end_time - start_time, 2)} seconds")

    if open_ports:
        print("Open Ports:", open_ports)
    else:
        print("No open ports found.")


# Main Program
target = input("Enter target IP or domain: ").strip()

try:
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    # Input validation (important improvement)
    if start_port < 0 or end_port > 65535 or start_port > end_port:
        print("❌ Invalid port range. Use 0–65535.")
    else:
        scan_ports(target, start_port, end_port)

except ValueError:
    print("❌ Please enter valid numeric port values.")