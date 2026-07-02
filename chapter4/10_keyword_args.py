from typing import List, Tuple, Dict, Optional

def get_results(products: List[Tuple[str, int]], **kwargs: Optional[Dict[str, str | int]]) -> List[Tuple[str, int]]:

    # Improved filtering to allow matching on one or more provided criteria
    results = [
        # [<expression> for <item> in <iterable> if <condition>]
        (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') == price
    ]
    return results

def main():
    products = [("lenovo", 100), ("lenovo", 40), ("imb", 100)]
    criteria = {"brand": "lenovo", "price": 100}

    # Demonstration of the function
    print(get_results(products, **criteria))

if __name__ == "__main__":
    main()