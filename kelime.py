from unicode_tr import unicode_tr
lines = []
with open("Turkce-Kelime-Listesi.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open('5HarfliKelimeListesi.txt', 'w+', encoding='utf-8') as words:
    line = lines[-1]
    c = line[5:6]
    for line in lines:
        new_line = (line.replace(c, "")).strip()
        karakter = len(new_line)
        if karakter == 5:
            text_true = unicode_tr(new_line)
            upperKelime = text_true.upper()+"\n"
            words.write(upperKelime)
