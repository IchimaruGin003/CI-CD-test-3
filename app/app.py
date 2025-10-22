def dedupe(items):
    """Remove duplicates from list while preserving order"""
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item

def add_numbers(a, b):
    """Add two numbers together"""
    return a + b

if __name__ == "__main__":
    # 原有的去重演示
    sample_data = [1, 2, 2, 3, 4, 4, 5]
    result = list(dedupe(sample_data))
    print(f"Original: {sample_data}")
    print(f"Deduplicated: {result}")
    
    # 新功能演示
    sum_result = add_numbers(5, 3)
    print(f"Addition: 5 + 3 = {sum_result}")