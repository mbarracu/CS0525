import re
from datetime import datetime, date

def assistente_virtuale(comando):
    # Normalizzo l'input
    comando = comando.strip().lower()

    # Pattern regex per riconoscere le intenzioni
    pattern_data = r"\bdata\b"
    pattern_ora = r"\bora\b"
    pattern_nome = r"(come ti chiami|chi sei|il tuo nome|nome)"

    # Caso combinato: l'utente chiede sia data che ora
    if re.search(pattern_data, comando) and re.search(pattern_ora, comando):
        oggi = date.today()
        ora_attuale = datetime.now().time()
        risposta_data = oggi.strftime("%d/%m/%Y")
        risposta_ora = ora_attuale.strftime("%H:%M")
        return f"Oggi è {risposta_data} e sono le {risposta_ora}."

    # Solo data
    elif re.search(pattern_data, comando):
        oggi = date.today()
        return "La data di oggi è " + oggi.strftime("%d/%m/%Y")

    # Solo ora
    elif re.search(pattern_ora, comando):
        ora_attuale = datetime.now().time()
        return "Sono le " + ora_attuale.strftime("%H:%M")

    # Nome assistente (più varianti grazie alle regex)
    elif re.search(pattern_nome, comando):
        return "Mi chiamo Colonnello Filippo Petrucci, io con le mie due lauree so fornire ora e data locale."

    # Nessun pattern riconosciuto
    else:
        return "Non ho capito la tua domanda."


def main():
    print("Assistente Virtuale")
    print("-------------------")

    first_interaction = True

    while True:
        if first_interaction:
            comando_utente = input(
                "Ciao! Sono il tuo assistente virtuale. Cosa vuoi sapere?\n"
                "...sono un orologio con la data di base...fai tu...\n"
                "...non chiedermi come mi chiamo...\n"
                "(exit per uscire): "
            ).strip()

            print()
            first_interaction = False
        else:
            print()
            comando_utente = input(
                "Hai altre domande?\n"
                "(esci/exit per uscire): "
            ).strip()

        # Gestione input vuoto
        if comando_utente == "":
            print("Per favore scrivi qualcosa.")
            continue

        # Comando di uscita normalizzato (accetta sia 'esci' che 'exit')
        if comando_utente.lower() in ("exit", "esci"):
            print("Arrivederci!")
            break

        print(assistente_virtuale(comando_utente))

# main viene eseguito solo se lo script è eseguito direttamente
if __name__ == "__main__":
    main()

# ---------------------------------------------------------------
# DESCRIZIONE DEL CODICE MIGLIORATO
#
# Il programma implementa un semplice assistente virtuale capace
# di fornire la data, l’ora oppure entrambe, in base alla richiesta
# dell’utente.
#
# La versione originale presentava errori logici, sintattici e di
# utilizzo della libreria datetime. Questa versione aggiornata
# corregge tali problemi e introduce i seguenti miglioramenti:
#
# - Input normalizzato con .strip().lower() per gestire variazioni
#   di maiuscole/minuscole e spazi indesiderati.
#
# - Riconoscimento basato su parole chiave, più flessibile rispetto
#   a confronti rigidi con frasi predefinite.
#
# - Gestione del caso combinato, quando l’utente richiede sia
#   la data sia l’ora contemporaneamente.
#
# - Gestione dell’input vuoto per evitare comportamenti imprevisti
#   o cicli inutili.
#
# - Struttura più chiara grazie all’introduzione di una funzione
#   main() che contiene il ciclo principale di interazione.
#
# - Risposta predefinita per domande non riconosciute, così da
#   mantenere un comportamento coerente.
#
# - Comando di uscita robusto ("exit"), riconosciuto in qualsiasi
#   combinazione di maiuscole/minuscole.
#
# - Vengono utilizzate espressioni regolari (regex)
#   per riconoscere in modo più accurato le parole chiave nelle richieste.
# ---------------------------------------------------------------
