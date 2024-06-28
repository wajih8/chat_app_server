const exp = require("express");
const spaw = require("child_process").spawn;
const bp = require("body-parser");
app = exp();
app.use(bp.urlencoded({ extended: true }));
app.get("/", (req, rep) => {
  rep.status("200").send("3aslema MR, madam");
});

app.get("/wajih", (req, rep) => {
  const pys = spaw("python", ["./hey.py", JSON.stringify()]);
  pys.stdout.on("data", (data) => {
    x = JSON.parse(data.toString());
    console.log(x);
    rep.send(x);
  });
});
// mana3arich 3leha chta3mil :)
app.post("/getAllFriends", (req, rep) => {
  x = req.body;
  const pys = spaw("python", [
    "./functions/serch_for_friends.py",
    JSON.stringify(x),
  ]);

  pys.stdout.on("data", (data) => {
    y = JSON.parse(data.toString());
    rep.send(y);
  });
});
// this post request to search for a user that the app user search for.
// the way it work is get the name of user like {name:"example"} and send it to search_for_friends.py .
// it return { error: 'no user found' } if no user found .
// or return { id: 123, unid: 'abc123', name: 'example' } if the user exist .
app.post("/serchfriend", (req, rep) => {
  //lihna n7athrou requset li bich nab3thoha lil python .
  const pys = spaw("python", [
    "./functions/serch_for_friends.py",
    JSON.stringify(req.body),
  ]);
  //lihna na5thou resulta ta3 l execution ta3 script .
  pys.stdout.on("data", (data) => {
    //lihna naba3thou l result lil application li jitna minha reques <3 .
    rep.send(JSON.parse(data.toString()));
  });
});

app.listen(3000, () => {
  console.log("server run on http://localhost:3000");
});
