# main.py
# --------------------
# Main program for testing Password Validator

from passwordValidator import PasswordValidator


def showReport(rep):
    print("----------------------------------")

    if rep["valid"]:
        print("Password VALID")
        print("----------------------------------")
        return

    print("Password INVALID")
    print(f"- length: {rep['len']} (OK: {rep['lenOK']})")

    if not rep["allowChar"]:
        print(f"- invalid chars: {', '.join(rep['badChars'])}")

    # show missing conditions
    miss = [e for e in rep["errors"] if e.startswith("missing_")]
    if miss:
        print("- missing:")
        for m in miss:
            print("  *", m)

    print("----------------------------------")


def main():
    validator = PasswordValidator()

    try:
        pw = input("Enter password: ")
    except KeyboardInterrupt:
        print("\nInput cancelled by user")
        return
    
    rep = validator.validate(pw)
    showReport(rep)


if __name__ == "__main__":
    main()
