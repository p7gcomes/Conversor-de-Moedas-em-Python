import argparse
from converter import convert_currency

def main():
    parser = argparse.ArgumentParser(description="Conversor de Moedas")
    parser.add_argument("--from", dest="from_currency", required=True, help="Moeda de origem (ex: USD)")
    parser.add_argument("--to", dest="to_currency", required=True, help="Moeda de destino (ex: BRL)")
    parser.add_argument("--amount", type=float, required=True, help="Valor a converter")

    args = parser.parse_args()

    try:
        result = convert_currency(args.amount, args.from_currency, args.to_currency)
        print(f"{args.amount:.2f} {args.from_currency.upper()} = {result:.2f} {args.to_currency.upper()}")
    except Exception as e:
        print("Erro ao converter moeda:", e)

if __name__ == "__main__":
    main()
