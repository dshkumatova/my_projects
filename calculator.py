import argparse

parser = argparse.ArgumentParser(description="Калькулятор")
parser.add_argument("a", type=float, help="первое число")
parser.add_argument("op", choices=["+", "-", "x", "/"], help="операция")
parser.add_argument("b", type=float, help="второе число")
args = parser.parse_args()

if args.op == "+":
    result = args.a + args.b
elif args.op == "-":
    result = args.a - args.b
elif args.op == "x":
    result = args.a * args.b
else:
    if args.b == 0:
        print("Ошибка: деление на ноль")
        raise SystemExit(1)
    result = args.a / args.b

print(f"{args.a} {args.op} {args.b} = {result}")
