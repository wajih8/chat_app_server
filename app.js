const exp = require("express");
const spaw = require("child_process").spawn;
const bp = require("body-parser");
app = exp();
app.use(bp.urlencoded({ extended: true }));
app.get("/", (req, rep) => {
  rep.status("200").send("3aslema MR, madam");
  console.log("------------------------------------------");
});

app.get("/wajih", (req, rep) => {
  const pys = spaw("python", ["./hey.py", JSON.stringify()]);
  pys.stdout.on("data", (data) => {
    x = JSON.parse(data.toString());
    console.log(x);
    rep.send(x);
    console.log("------------------------------------------");
  });
});
// mana3arich 3leha chta3mil :)
app.post("/getAllFriends", (req, rep) => {
  x = req.body;
  console.log(
    "-----------------------------\nchecking frindes with this data :"
  );
  console.log(x);

  const pys = spaw("python", [
    "./functions/serch_for_friends.py",
    JSON.stringify(x),
  ]);

  pys.stdout.on("data", (data) => {
    y = JSON.parse(data.toString());
    console.log("friends data:");
    console.log(y);
    console.log("------------------------------------------");
    rep.send(y);
    console.log("friends sended");
    console.log("------------------------------------------");
  });
});
// this post request to search for a user that the app user search for.
// the way it work is get the name of user like {name:"example"} and send it to search_for_friends.py .
// it return { error: 'no user found' } if no user found .
// or return { id: 123, unid: 'abc123', name: 'example' } if the user exist .
app.post("/serchfriend", (req, rep) => {
  //lihna n7athrou requset li bich nab3thoha lil python .
  const pys = spaw("python", [
    "./functions/serch.py",
    JSON.stringify(req.body),
  ]);
  console.log(req.body);
  //lihna na5thou resulta ta3 l execution ta3 script .
  pys.stdout.on("data", (data) => {
    //lihna naba3thou l result lil application li jitna minha reques <3 .
    console.log("------------------------------------------");
    rep.send(JSON.parse(data.toString()));
  });
});

app.post("/getchat", (req, rep) => {
  //lihna n7athrou requset li bich nab3thoha lil python .
  const pys = spaw("python", [
    "./functions/getchat.py",
    JSON.stringify(req.body),
  ]);
  //lihna na5thou resulta ta3 l execution ta3 script .
  pys.stdout.on("data", (data) => {
    console.log("data sended");
    console.log("------------------------------------------");
    //lihna naba3thou l result lil application li jitna minha reques <3 .
    rep.send(JSON.parse(data.toString()));
  });
});
app.post("/send_message", (req, rep) => {
  //lihna n7athrou requset li bich nab3thoha lil python .
  const pys = spaw("python", [
    "./functions/messagesent.py",
    JSON.stringify(req.body),
  ]);
  console.log(req.body);
  //lihna na5thou resulta ta3 l execution ta3 script .
  pys.stdout.on("data", (data) => {
    console.log("data inserted secsessfuly");
    console.log("------------------------------------------");
    //lihna naba3thou l result lil application li jitna minha reques <3 .
    rep.send(JSON.parse(data.toString()));
  });
});

app.post("/checkcoockie", (req, rep) => {
  //lihna n7athrou requset li bich nab3thoha lil python .
  const pys = spaw("python", [
    "./functions/chechcoockie.py",
    JSON.stringify(req.body),
  ]);
  console.log(
    "-----------------------------\nchecking coockie with this data :"
  );
  console.log(req.body);
  //lihna na5thou resulta ta3 l execution ta3 script .
  pys.stdout.on("data", (data) => {
    console.log("data checked secsessfuly");
    console.log("------------------------------------------");
    //lihna naba3thou l result lil application li jitna minha request <3 .
    rep.send(JSON.parse(data.toString()));
  });
});

app.post("/check_login", (req, rep) => {
  //lihna n7athrou requset li bich nab3thoha lil python .
  const pys = spaw("python", [
    "./functions/login.py",
    JSON.stringify(req.body),
  ]);
  console.log("-----------------------------\nchecking login with this data :");
  console.log(req.body);
  //lihna na5thou resulta ta3 l execution ta3 script .
  pys.stdout.on("data", (data) => {
    console.log("login retrived");
    console.log(data.toString());
    console.log("------------------------------------------");
    //lihna naba3thou l result lil application li jitna minha reques <3 .
    rep.send(JSON.parse(data.toString()));
  });
});

app.post("/check_last_message", (req, rep) => {
  //lihna n7athrou requset li bich nab3thoha lil python .
  const pys = spaw("python", [
    "./functions/check_last_message.py",
    JSON.stringify(req.body),
  ]);
  console.log(req.body);
  //lihna na5thou resulta ta3 l execution ta3 script .
  pys.stdout.on("data", (data) => {
    console.log("message checked secsessfuly :");
    console.log(data.toString());
    console.log("------------------------------------------");

    //lihna naba3thou l result lil application li jitna minha reques <3 .
    rep.send(JSON.parse(data.toString()));
  });
});
app.post("/check_reqt", (req, rep) => {
  //lihna n7athrou requset li bich nab3thoha lil python .
  const pys = spaw("python", [
    "./functions/check_reqt.py",
    JSON.stringify(req.body),
  ]);
  console.log(req.body);
  //lihna na5thou resulta ta3 l execution ta3 script .
  pys.stdout.on("data", (data) => {
    console.log("request checked secsessfuly :");
    console.log(data.toString());
    console.log("------------------------------------------");

    //lihna naba3thou l result lil application li jitna minha reques <3 .
    rep.send(JSON.parse(data.toString()));
  });
});

app.post("/send_friend_req", (req, rep) => {
  //lihna n7athrou requset li bich nab3thoha lil python .
  const pys = spaw("python", [
    "./functions/send_friend_req.py",
    JSON.stringify(req.body),
  ]);
  console.log(
    "-----------------------------\nsend friend req with this data :"
  );
  console.log(req.body);
  //lihna na5thou resulta ta3 l execution ta3 script .
  pys.stdout.on("data", (data) => {
    console.log(data.toString());
    console.log("------------------------------------------");
    //lihna naba3thou l result lil application li jitna minha reques <3 .
    rep.send(JSON.parse(data.toString()));
  });
});

app.listen(3000, () => {
  console.log("server run on http://localhost:3000");
});
