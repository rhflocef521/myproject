class MyExcept(Exception):
    pass
    def show(self):
        print("haha")

if __name__ == '__main__':
        me=MyExcept()
        me.show()
        try:
            raise MyExcept
        except MyExcept as e:
            print("raise MyExcept")
            e.show()