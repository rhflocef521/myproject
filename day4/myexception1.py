if __name__ == '__main__':
   try:
        f=open("good.text","r")
        f.close()
   except FileNotFoundError as f:
       print()
       print("我能处理")
