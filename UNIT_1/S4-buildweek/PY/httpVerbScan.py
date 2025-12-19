import requests
from urllib.parse import urljoin

def test_methods(base_url: str, path: str):
    url = urljoin(base_url.rstrip("/") + "/", path.lstrip("/"))

    methods = ["OPTIONS", "GET", "POST", "PUT", "DELETE"]
    results = {}

    try:
        r = requests.options(url, timeout=5, allow_redirects=False)
        results["OPTIONS"] = (r.status_code, r.headers.get("Allow", ""), r.headers.get("Server", ""))
    except requests.RequestException as e:
        results["OPTIONS"] = ("ERR", str(e), "")

    payload = {"test": "1"}

    for m in ["GET", "POST", "PUT", "DELETE"]:
        try:
            if m == "GET":
                r = requests.get(url, timeout=5, allow_redirects=False)
            elif m == "POST":
                r = requests.post(url, data=payload, timeout=5, allow_redirects=False)
            elif m == "PUT":
                r = requests.put(url, data=payload, timeout=5, allow_redirects=False)
            elif m == "DELETE":
                r = requests.delete(url, timeout=5, allow_redirects=False)

            results[m] = (r.status_code, r.headers.get("Allow", ""), r.headers.get("Server", ""))
        except requests.RequestException as e:
            results[m] = ("ERR", str(e), "")

    print(f"\nTarget: {url}")
    print("-" * 70)
    for method, (code, allow, server) in results.items():
        allow_txt = f" Allow={allow}" if allow else ""
        server_txt = f" Server={server}" if server else ""
        print(f"{method:7} -> {code}{allow_txt}{server_txt}")


    enabled = []
    for method, (code, _, _) in results.items():
        if code == "ERR":
            continue
        
        if code != 405:
            enabled.append(method)

    print("\nLikely handled/enabled methods:", ", ".join(enabled) if enabled else "None / unclear")

def main():
    base_url = input("Base URL (e.g., http://192.168.50.101/): ").strip()
    path = input("Path (e.g., /dvwa/ or /phpMyAdmin/): ").strip()

    if not base_url:
        print("Base URL is required.")
        return

    if not path:
        path = "/"

    test_methods(base_url, path)

if __name__ == "__main__":
    main()
