def merge(*lists):
    # Simple merge: concatenate and sort by 'date' if available (descending)
    items = []
    for lst in lists:
        if not lst:
            continue
        items.extend(lst)
    try:
        items.sort(key=lambda x: x.get('date', ''), reverse=True)
    except Exception:
        pass
    return items
