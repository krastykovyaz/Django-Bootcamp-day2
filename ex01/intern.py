class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name
        self.emp_itrn = self.Coffee()
    
    def __str__(self):
        return self.name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.emp_itrn

    class Coffee:
        def  __str__(self):
            return "This is the worst coffee you ever tasted."

if __name__ == "__main__":
    # print(Intern())
    # print(Intern("Mark"))
    itrn = Intern("Mark")
    # itrn.make_coffee()
    emp_itrn = Intern()
    print(itrn.make_coffee())
    try:
        itrn.work()
        # emp_itrn.work()
    except Exception as e:
        print(e)