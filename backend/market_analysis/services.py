from .models import ProductPriceReference

def compare_product_price(product_name, current_price):
    refs = ProductPriceReference.objects.filter(product_name__iexact=product_name)
    return [{
        "supplier": r.supplier,
        "market_price": float(r.price),
        "current_price": current_price,
        "difference": round(current_price - float(r.price), 2),
        "source": r.source,
    } for r in refs]
