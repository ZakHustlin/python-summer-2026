file_name = input("Enter a file name: ").lower().strip()
if file_name.endswith(".pdf"):
    print("PDF file")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("JPEG image")
elif file_name.endswith(".png"):
    print("PNG image")
elif file_name.endswith(".txt"):
    print("Text file")
elif file_name.endswith(".zip"):
    print("ZIP archive")
elif file_name.endswith(".gif"):
    print("GIF image")
else:
    print("application/octet-stream")