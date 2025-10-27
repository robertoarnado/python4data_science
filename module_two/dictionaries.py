import copy

def main():
    # 1. Create dictionaries
    d1 = {"name": "Alice", "age": 30, "city": "Lisbon"}
    d2 = dict(language="Python", version=3.10)

    print("d1:", d1)
    print("d2:", d2)

    # 2. Access values
    print("Name (bracket):", d1["name"])
    print("Country (get with default):", d1.get("country", "Unknown"))

    # 3. Add / update entries
    d1["country"] = "Portugal"          # add
    d1["age"] = 31                      # update
    d1.update({"profession": "Engineer"})
    print("After add/update:", d1)

    # 4. setdefault — returns existing or sets default
    country = d1.setdefault("country", "NoCountry")
    language = d1.setdefault("language", "English")
    print("setdefault country:", country)
    print("setdefault language (added):", language)
    print("d1 now:", d1)

    # 5. Remove entries
    removed = d1.pop("profession", None)
    print("Removed profession:", removed)
    last_key, last_value = d1.popitem()  # removes an arbitrary (key,value) in older Py, last in 3.7+
    print("Popitem returned:", (last_key, last_value))
    # note: avoid popitem if you need deterministic removal across versions
    print("d1 after removals:", d1)

    # 6. Iteration
    for key in d1:
        print(f"key={key}, value={d1[key]}")

    for key, value in d2.items():
        print("d2 item:", key, "=", value)

    # 7. Keys / Values / Items views
    keys = d1.keys()
    values = d1.values()
    items = d1.items()
    print("keys view:", keys)
    print("values view:", values)
    print("items view:", items)

    # 8. Copying
    shallow = d1.copy()
    deep = copy.deepcopy(d1)
    shallow["name"] = "Bob"
    print("original after shallow change:", d1["name"], "shallow:", shallow["name"], "deep:", deep["name"])

    # 9. Merging dictionaries (Python 3.9+: | operator)
    merged = d1 | d2
    print("merged (d1 | d2):", merged)
    # or use update to merge into existing dict
    merged2 = dict(d1)
    merged2.update(d2)
    print("merged2 (update):", merged2)

    # 10. From keys and comprehensions
    keys_list = ["a", "b", "c"]
    fromkeys = dict.fromkeys(keys_list, 0)
    print("fromkeys:", fromkeys)

    squares = {n: n * n for n in range(6)}
    print("squares dict:", squares)

    # 11. Nested dictionaries
    users = {
        "alice": {"age": 30, "email": "alice@example.com"},
        "bob": {"age": 25, "email": "bob@example.com"},
    }
    print("alice email:", users["alice"]["email"])

    # 12. Safe nested access
    alice_email = users.get("alice", {}).get("email")
    carol_email = users.get("carol", {}).get("email", "no-email")
    print("safe alice email:", alice_email)
    print("safe carol email (default):", carol_email)

    # 13. Sorting by keys or values
    sorted_by_key = dict(sorted(squares.items()))  # sorts by key
    sorted_by_value = dict(sorted(squares.items(), key=lambda kv: kv[1]))  # by value
    print("sorted by key:", sorted_by_key)
    print("sorted by value:", sorted_by_value)

if __name__ == "__main__":
    main()