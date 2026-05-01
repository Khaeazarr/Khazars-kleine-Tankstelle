print("--- Willkommen an der Regensburg-Tankstelle ---")

kraftstoffe = {
    "1": ("Benzin Premium", 1.80),
    "2": ("Benzin Normal", 1.65),
    "3": ("Diesel Premium", 2.10),
    "4": ("Diesel Normal", 1.90)
}

shop_artikel = {
    "1": ("Wasser", 0.70),
    "2": ("Saft", 1.30),
    "3": ("Sneakers Schokolade", 1.40),
    "4": ("Burger", 3.50)
}

# 1. Kraftstoff wählen
print("\nKRAFTSTOFFE:")
for k, v in kraftstoffe.items():
    print(f"{k}: {v[0]} ({v[1]}€/L)")

wahl_k = input("Wähle Kraftstoff (1-4) oder 0 für keinen: ")
liter = 0
sprit_preis = 0

if wahl_k in kraftstoffe:
    liter = float(input(f"Wie viele Liter {kraftstoffe[wahl_k][0]}? "))
    sprit_preis = liter * kraftstoffe[wahl_k][1]

# 2. Shop Artikel
print("\nKIOSK-ARTIKEL:")
for k, v in shop_artikel.items():
    print(f"{k}: {v[0]} ({v[1]}€)")

shop_summe = 0
while True:
    wahl_s = input("Wähle Artikel (1-4) zum Hinzufügen oder 'n' für Ende: ")
    if wahl_s == 'n':
        break
    if wahl_s in shop_artikel:
        shop_summe += shop_artikel[wahl_s][1]
        print(f"-> {shop_artikel[wahl_s][0]} hinzugefügt.")

# 3. Quittung
gesamt = sprit_preis + shop_summe
print("\n" + "="*30)
print("RECHNUNG / QUITTUNG")
if sprit_preis > 0:
    print(f"Kraftstoff: {liter}L zu {kraftstoffe[wahl_k][1]}€ = {sprit_preis:.2f}€")
print(f"Shop-Einkauf: {shop_summe:.2f}€")
print("-" * 30)
print(f"GESAMTBETRAG: {gesamt:.2f}€")
print("="*30)
print("Vielen Dank für Ihren Besuch!")
