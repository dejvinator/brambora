from db import connect

def vypis_okresu():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id_okres, nazev FROM okresy ORDER BY id_okres")

    for row in cur.fetchall():
        print(row[0], row[1])

    conn.close()


def obce_v_okrese():
    kod = input("Zadej kód okresu: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT nazev, pocet_obyvatel, prumerny_vek
        FROM obce_pob
        WHERE id_okres = %s
    """, (kod,))

    for r in cur.fetchall():
        print(r)

    conn.close()


def hledani_obce():
    text = input("Zadej název: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT nazev
        FROM obce_pob
        WHERE LOWER(nazev) LIKE LOWER(%s)
    """, (f"%{text}%",))

    for r in cur.fetchall():
        print(r[0])

    conn.close()


def statistika_okresu():
    kod = input("Zadej kód okresu: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            SUM(pocet_obyvatel),
            AVG(prumerny_vek),
            SUM(pocet_muzi),
            SUM(pocet_zeny)
        FROM obce_pob
        WHERE id_okres = %s
    """, (kod,))

    data = cur.fetchone()

    print("Obyvatelé:", data[0])
    print("Věk:", round(data[1], 2))
    print("Muži:", data[2])
    print("Ženy:", data[3])