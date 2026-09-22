# match
# Python's structural pattern matching.
# It is somewhat similar to switch in other languages.
status = 200

match status:

    case 200:
        print("OK")

    case 404:
        print("Not Found")

    case 500:
        print("Server Error")