const spaw = require("child_process").spawn;

const data = ["wa basas"];
const pys = spaw("python", ["./hey.py"]);
pys.stdout.on("data", (data) => {
  x = JSON.parse(data.toString());

  console.log(x.wa);
});
