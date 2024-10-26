const spaw = require("child_process").spawn;
x = {
  id: 157,
  uniqueid: "uqsqd4421a4q",
  username: "wajih",
  validation: "j2l923f2iL19eda918kClvmHe6",
};
z = JSON.stringify(x);
console.log(z);
const pys = spaw("python", ["./functions/serch_for_friends.py", z]);
pys.stdout.on("data", (data) => {
  y = data.toString();
  console.log(y);
});
