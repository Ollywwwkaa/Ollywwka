def make_bold (fun):
    def wrapper():
        text = fun()
        return f"<b> {text} </b> "
    return wrapper
@make_bold 
def text1() :
    return "Hello, World!"
print(text1())