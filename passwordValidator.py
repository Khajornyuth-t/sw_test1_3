# passwordValidator.py
# --------------------
# Password Validator (single-pass)

from string import ascii_lowercase, ascii_uppercase, digits


class PasswordValidator:
    # Base Define
    MIN_LEN = 8
    MAX_LEN = 20
    SPECIAL_CHARS = "!@#$%^&*()_+="

    def __init__(self, minLen=MIN_LEN, maxLen=MAX_LEN, specials=SPECIAL_CHARS):
        self.minLen = minLen
        self.maxLen = maxLen
        self.specials = specials

        # whitelist set for check quick membership (O(1))
        self.whitelistSet = set(ascii_lowercase + ascii_uppercase + digits + specials)
        self.specialSet = set(specials)

    def validate(self, pw):
        if pw is None:
            pw = ""

        pwLen = len(pw)

        # template for result
        result = {
            "valid": False,
            "len": pwLen,
            "lenOK": (self.minLen <= pwLen <= self.maxLen),

            "allowChar": True,

            "hasLower": False,
            "hasUpper": False,
            "hasDigit": False,
            "hasSpecial": False,

            "badChars": [],   # Keep order of appearance
            "errors": []
        }

        # flag for check condition within loop
        seenBad = set()
        flagLower = False
        flagUpper = False
        flagDigit = False
        flagSpecial = False

        # loop single pass
        for ch in pw:

            # character is valid
            if ch in self.whitelistSet:

                # check character type
                if not flagLower and ('a' <= ch <= 'z'):
                    flagLower = True
                elif not flagUpper and ('A' <= ch <= 'Z'):
                    flagUpper = True
                elif not flagDigit and ('0' <= ch <= '9'):
                    flagDigit = True
                elif not flagSpecial and (ch in self.specialSet):
                    flagSpecial = True

            else:
                # character is invalid
                if ch not in seenBad:
                    seenBad.add(ch)
                    result["badChars"].append(ch)

                result["allowChar"] = False

        # update flag to result
        result["hasLower"] = flagLower
        result["hasUpper"] = flagUpper
        result["hasDigit"] = flagDigit
        result["hasSpecial"] = flagSpecial

        # check error code
        if not result["lenOK"]:
            result["errors"].append("length")

        if not flagLower:
            result["errors"].append("missing_lower")
        if not flagUpper:
            result["errors"].append("missing_upper")
        if not flagDigit:
            result["errors"].append("missing_digit")
        if not flagSpecial:
            result["errors"].append("missing_special")

        if not result["allowChar"]:
            result["errors"].append("invalid_char")

        # summary valid
        result["valid"] = (
            result["lenOK"] and
            result["allowChar"] and
            flagLower and flagUpper and flagDigit and flagSpecial
        )

        return result
