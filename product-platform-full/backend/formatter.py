def toman(price):
    try:
        return f"{int(float(price)):,}".replace(",", "٬") + " تومان"
    except:
        return "نامشخص"
