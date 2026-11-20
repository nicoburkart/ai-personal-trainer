#!/usr/bin/env python3
"""Look up protein, calories and macros per 100 g in Open Food Facts (free, no key, worldwide).

  python3 food.py barcode <ean>                     # one product by its barcode
  python3 food.py search <words...> [--country es]  # top matches by name, optionally in one country

Prints JSON. On failure prints {"error": ...} and exits 1. Sends no personal data: only the barcode or the
search words. Fresh and weighed products (store barcodes starting with 2) are usually missing; read their label.
Open Food Facts allows about 10 searches a minute, so searches wait until 6.5 s after the previous one.
"""
import json, os, sys, tempfile, time, urllib.error, urllib.parse, urllib.request

UA = {"User-Agent": "ai-personal-trainer/0.2 (personal nutrition lookups)"}
FIELDS = "code,product_name,brands,quantity,nutriments"
STAMP = os.path.join(tempfile.gettempdir(), "ai-personal-trainer-off-search")
GAP = 6.5


def fail(msg):
    print(json.dumps({"error": msg})); sys.exit(1)


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(10 * (i + 1)); continue
            fail(f"Open Food Facts answered HTTP {e.code}; try again in a minute")
        except (urllib.error.URLError, TimeoutError) as e:
            if i < tries - 1:
                time.sleep(5); continue
            fail(f"couldn't reach Open Food Facts ({e}); check the internet connection")
        except json.JSONDecodeError:
            if i < tries - 1:
                time.sleep(10 * (i + 1)); continue
            fail("Open Food Facts sent an error page instead of data; try again in a minute")


def kcal(n):
    v = n.get("energy-kcal_100g")
    if v is None and n.get("energy-kj_100g") is not None:
        v = round(n["energy-kj_100g"] / 4.184, 1)
    return v


def shape(p):
    n = p.get("nutriments", {})
    return {
        "barcode": p.get("code"), "name": p.get("product_name"), "brand": p.get("brands"), "pack": p.get("quantity"),
        "per_100g": {"kcal": kcal(n), "protein_g": n.get("proteins_100g"), "carbs_g": n.get("carbohydrates_100g"),
                     "fat_g": n.get("fat_100g"), "fiber_g": n.get("fiber_100g")},
    }


def complete(row):
    return row["per_100g"]["kcal"] is not None and row["per_100g"]["protein_g"] is not None


def pace():
    try:
        wait = GAP - (time.time() - os.path.getmtime(STAMP))
        if wait > 0:
            time.sleep(wait)
    except OSError:
        pass
    open(STAMP, "w").close()


def main(argv):
    if len(argv) < 2 or argv[0] not in ("barcode", "search"):
        print(__doc__); return 2
    if argv[0] == "barcode":
        d = get(f"https://world.openfoodfacts.org/api/v2/product/{urllib.parse.quote(argv[1])}.json?fields={FIELDS}")
        if not d or d.get("status") != 1:
            print(json.dumps({"found": False, "barcode": argv[1]})); return 0
        row = shape(d["product"])
        print(json.dumps({"found": True, "complete": complete(row), **row}, ensure_ascii=False, indent=1)); return 0
    words, country, it = [], None, iter(argv[1:])
    for a in it:
        if a == "--country": country = next(it, None)
        else: words.append(a)
    q = {"search_terms": " ".join(words), "search_simple": 1, "action": "process", "json": 1, "page_size": 10, "fields": FIELDS}
    if country:
        q.update({"tagtype_0": "countries", "tag_contains_0": "contains", "tag_0": country})
    pace()
    d = get("https://world.openfoodfacts.org/cgi/search.pl?" + urllib.parse.urlencode(q)) or {}
    rows = [r for r in (shape(p) for p in d.get("products", [])) if complete(r)]
    print(json.dumps({"query": " ".join(words), "country": country, "results": rows[:6]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
