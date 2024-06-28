import requests as reqs

y = 0
"""while y < 5:
    try:

        da = {"name": "wajih", "age": 19}
        x1 = reqs.get("http://localhost:3000/"
                      )
        print(x1.content.decode("utf-8"))
        y = 10

    except:
        y += 1
        time.sleep(3)
        print(y)"""
da = {"name": "wajih", "age": 19}
x1 = reqs.post("http://localhost:3000/checkuser", data=da
               )


print(x1.json())
