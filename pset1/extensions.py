# Prompt user for file name
file = input("File name: ")

# Decision making
match file:
    case _ if file.endswith(".gif"):
        print("image/gif")
    case _ if file.endswith(".jpg"):
        print("image/jpg")
    case _ if file.endswith(".jpeg"):
        print("image/jpeg")
    case _ if file.endswith(".png"):
        print("image/png")
    case _ if file.endswith(".pdf"):
        print("application/pdf")
    case _ if file.endswith(".txt"):
        print("text/plain")
    case _ if file.endswith(".zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")
