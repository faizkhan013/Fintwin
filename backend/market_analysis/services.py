from .models import ProductPriceReference


def compare_product_price(product_name, current_price=0):
    refs = list(ProductPriceReference.objects.filter(product_name__iexact=product_name).order_by("price"))
    if not refs:
        return {
            "product": product_name or "No product selected",
            "yourPrice": float(current_price or 0),
            "marketLow": 0,
            "marketHigh": 0,
            "marketAvg": 0,
            "rating": "No reference data",
            "references": [],
        }
    prices = [float(r.price) for r in refs]
    current = float(current_price or 0)
    avg = sum(prices) / len(prices)
    if not current:
        current = avg
    ratio = current / avg if avg else 1
    rating = "Below market" if ratio < 0.9 else "Above market" if ratio > 1.1 else "Fairly priced"
    return {
        "product": product_name,
        "yourPrice": current,
        "marketLow": min(prices),
        "marketHigh": max(prices),
        "marketAvg": round(avg, 2),
        "rating": rating,
        "references": [{"supplier": r.supplier, "price": float(r.price), "source": r.source} for r in refs],
    }
