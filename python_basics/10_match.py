def httpCodes(status):
    match status:
        case 400:
            return "bad request"
        case 401 | 403 :
             return "Unauthorized"
        case 404:
            return "Not found"
        case 500:
            return "server error"
        case _:
            return "something went wrong with  the internet"

