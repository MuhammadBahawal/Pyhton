# similar to switch statement



def check_status(code):
    match code:
        case 200:
            print("Success")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case _:
            print("Unknown Status")

check_status(200) 
check_status(500)
