def dedupe(items):
    """Remove duplicates from list while preserving order"""
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item

if __name__ == "__main__":
    sample_data = [1, 2, 2, 3, 4, 4, 5]
    result = list(dedupe(sample_data))
    print(f"Original: {sample_data}")
    print(f"Deduplicated: {result}")
