
def checkSuccess(success:bool) -> bool:
    if not success:
        print("Camera is not available!")
        return False
    return True