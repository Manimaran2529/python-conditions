a=input("enter a query to check ,checkbalance,withdraw,deposit:").lower()
match a:
    case "checkbalance":
        print("80000")
    case "withdraw":
        b=int(input("enter a withdraw amount:"))
        if b<=80000:
            print("withdraw successfully")
        else:
            print("insuffient balance")
    case "deposit":
        deposit=int(input("enter a desposit amount"))
        print(deposit,"successfully")
    case _:
        print("enter a vaild query")